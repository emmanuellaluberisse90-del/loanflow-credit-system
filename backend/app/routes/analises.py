from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas
from ..services.analise import realizar_pre_analise
from datetime import date
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/analises",
    tags=["Análises"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.AnaliseResponse)
def criar_analise(
    id_solicitacao: int,
    db: Session = Depends(get_db)
):
    solicitacao = db.query(models.Solicitacao).filter(
        models.Solicitacao.id == id_solicitacao
    ).first()

    if solicitacao is None:
        raise HTTPException(
            status_code=404,
            detail="Solicitação não encontrada"
        )

    perfil = db.query(models.PerfilFinanceiro).filter(
        models.PerfilFinanceiro.id_cliente == solicitacao.id_cliente
    ).first()

    if perfil is None:
        raise HTTPException(
            status_code=404,
            detail="Perfil financeiro não encontrado"
        )

    resultado = realizar_pre_analise(
        renda_mensal=perfil.renda_mensal,
        despesas_mensais=perfil.despesas_mensais,
        parcelas_atuais=0,
        historico_pagamentos=perfil.historico_pagamentos,
        atrasos_ultimos_12m=perfil.atrasos_ultimos_12m
    )

    nova_analise = models.Analise(
        id_solicitacao=solicitacao.id,
        identidade_verificada="sim",
        cadastro_ativo="sim",
        renda_compativel=str(resultado["renda_compativel"]),
        historico_compativel=str(resultado["historico_compativel"]),
        comprometimento_renda=resultado["comprometimento_renda"],
        valor_maximo_simulado=resultado["valor_maximo_simulado"],
        resultado=resultado["resultado"],
        motivo_resultado=resultado["motivo_resultado"],
        data_analise=date.today()
    )

    db.add(nova_analise)
    db.commit()
    db.refresh(nova_analise)

    return nova_analise