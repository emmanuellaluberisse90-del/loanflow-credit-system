from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models


router = APIRouter(
    prefix="/agendamentos",
    tags=["Agendamentos"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def criar_agendamento(
    id_cliente: int,
    id_solicitacao: int,
    id_agencia: int,
    id_horario: int,
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == id_cliente
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    solicitacao = db.query(models.Solicitacao).filter(
        models.Solicitacao.id == id_solicitacao
    ).first()

    if solicitacao is None:
        raise HTTPException(
            status_code=404,
            detail="Solicitação não encontrada"
        )
    if solicitacao.id_cliente != id_cliente:
       raise HTTPException(
          status_code=400,
          detail="A solicitação não pertence ao cliente informado"
        )

    agendamento_existente = db.query(models.Agendamento).filter(
    models.Agendamento.id_solicitacao == id_solicitacao,
    models.Agendamento.status == "agendado"
    ).first()

    if agendamento_existente is not None:
       raise HTTPException(
          status_code=400,
          detail="A solicitação já possui um agendamento ativo"
        )

    agencia = db.query(models.Agencia).filter(
        models.Agencia.id == id_agencia
    ).first()

    if agencia is None:
        raise HTTPException(
            status_code=404,
            detail="Agência não encontrada"
        )

    horario = db.query(models.Horario).filter(
        models.Horario.id == id_horario
    ).first()

    if horario is None:
        raise HTTPException(
            status_code=404,
            detail="Horário não encontrado"
        )

    if horario.id_agencia != id_agencia:
       raise HTTPException(
          status_code=400,
          detail="O horário não pertence à agência informada"
        )

    if horario.disponivel != "sim":
        raise HTTPException(
            status_code=400,
            detail="Horário não está disponível"
        )

    novo_agendamento = models.Agendamento(
        id_cliente=id_cliente,
        id_solicitacao=id_solicitacao,
        id_agencia=id_agencia,
        id_horario=id_horario,
        data_agendamento=horario.data,
        status="agendado"
    )

    horario.disponivel = "nao"

    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)

    return novo_agendamento

@router.get("/")
def listar_agendamentos(
    db: Session = Depends(get_db)
):
    agendamentos = db.query(models.Agendamento).all()

    resultado = []

    for agendamento in agendamentos:

        cliente = db.query(models.Cliente).filter(
            models.Cliente.id == agendamento.id_cliente
        ).first()

        agencia = db.query(models.Agencia).filter(
            models.Agencia.id == agendamento.id_agencia
        ).first()

        horario = db.query(models.Horario).filter(
            models.Horario.id == agendamento.id_horario
        ).first()

        solicitacao = db.query(models.Solicitacao).filter(
            models.Solicitacao.id == agendamento.id_solicitacao
        ).first()

        resultado.append({
            "id_agendamento": agendamento.id,
            "cliente": cliente.nome if cliente else None,
            "solicitacao": solicitacao.id if solicitacao else None,
            "agencia": agencia.nome_agencia if agencia else None,
            "cidade_agencia": agencia.cidade if agencia else None,
            "data": str(horario.data) if horario else None,
            "hora_inicio": horario.hora_inicio if horario else None,
            "hora_fim": horario.hora_fim if horario else None,
            "status": agendamento.status
        })

    return resultado

@router.get("/{id_agendamento}")
def buscar_agendamento(
    id_agendamento: int,
    db: Session = Depends(get_db)
):
    agendamento = db.query(models.Agendamento).filter(
        models.Agendamento.id == id_agendamento
    ).first()

    if agendamento is None:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )

    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == agendamento.id_cliente
    ).first()

    agencia = db.query(models.Agencia).filter(
        models.Agencia.id == agendamento.id_agencia
    ).first()

    horario = db.query(models.Horario).filter(
        models.Horario.id == agendamento.id_horario
    ).first()

    solicitacao = db.query(models.Solicitacao).filter(
        models.Solicitacao.id == agendamento.id_solicitacao
    ).first()

    return {
        "id_agendamento": agendamento.id,
        "cliente": cliente.nome if cliente else None,
        "solicitacao": solicitacao.id if solicitacao else None,
        "agencia": agencia.nome_agencia if agencia else None,
        "cidade_agencia": agencia.cidade if agencia else None,
        "data": str(horario.data) if horario else None,
        "hora_inicio": horario.hora_inicio if horario else None,
        "hora_fim": horario.hora_fim if horario else None,
        "status": agendamento.status
    }

@router.put("/{id_agendamento}/cancelar")
def cancelar_agendamento(
    id_agendamento: int,
    db: Session = Depends(get_db)
):
    agendamento = db.query(models.Agendamento).filter(
        models.Agendamento.id == id_agendamento
    ).first()

    if agendamento is None:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado"
        )

    if agendamento.status == "cancelado":
        raise HTTPException(
            status_code=400,
            detail="Agendamento já está cancelado"
        )

    horario = db.query(models.Horario).filter(
        models.Horario.id == agendamento.id_horario
    ).first()

    if horario is None:
        raise HTTPException(
            status_code=404,
            detail="Horário não encontrado"
        )

    # Cancela o agendamento
    agendamento.status = "cancelado"

    # Libera novamente o horário
    horario.disponivel = "sim"

    db.commit()
    db.refresh(agendamento)

    return {
        "id_agendamento": agendamento.id,
        "status": agendamento.status,
        "horario_liberado": horario.disponivel
    }