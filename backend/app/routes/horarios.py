from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models


router = APIRouter(
    prefix="/horarios",
    tags=["Horários"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def criar_horario(
    id_agencia: int,
    data: date,
    hora_inicio: str,
    hora_fim: str,
    disponivel: str,
    db: Session = Depends(get_db)
):
    agencia = db.query(models.Agencia).filter(
        models.Agencia.id == id_agencia
    ).first()

    if agencia is None:
        raise HTTPException(
            status_code=404,
            detail="Agência não encontrada"
        )

    novo_horario = models.Horario(
        id_agencia=id_agencia,
        data=data,
        hora_inicio=hora_inicio,
        hora_fim=hora_fim,
        disponivel=disponivel
    )

    db.add(novo_horario)
    db.commit()
    db.refresh(novo_horario)

    return novo_horario

@router.get("/")
def listar_horarios(
    id_agencia: int,
    db: Session = Depends(get_db)
):
    horarios = db.query(models.Horario).filter(
        models.Horario.id_agencia == id_agencia,
        models.Horario.disponivel == "sim"
    ).all()

    return horarios