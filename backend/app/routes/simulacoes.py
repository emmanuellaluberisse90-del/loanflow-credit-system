from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas
from ..services.simulacao import (
    calcular_parcela,
    calcular_valor_total,
    verificar_capacidade_parcela
)

router = APIRouter(
    prefix="/simulacoes",
    tags=["Simulações"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.SimulacaoResponse)
def criar_simulacao(
    simulacao: schemas.SimulacaoCreate,
    db: Session = Depends(get_db)
):
    solicitacao = db.query(models.Solicitacao).filter(
        models.Solicitacao.id == simulacao.id_solicitacao
    ).first()

    perfil = db.query(models.PerfilFinanceiro).filter(
    models.PerfilFinanceiro.id_cliente == solicitacao.id_cliente
    ).first()

    if perfil is None:
        raise HTTPException(
           status_code=404,
           detail="Perfil financeiro não encontrado"
        )

    if solicitacao is None:
        raise HTTPException(
            status_code=404,
            detail="Solicitação não encontrada"
        )

    valor_parcela = calcular_parcela(
        simulacao.valor_simulado,
        simulacao.prazo_meses,
        simulacao.taxa_mensal
    )

    valor_total = calcular_valor_total(
        valor_parcela,
        simulacao.prazo_meses
    )

    parcela_maxima = perfil.renda_mensal * 0.30

    parcela_compativel = "True" if verificar_capacidade_parcela(
       valor_parcela,
       parcela_maxima
    ) else "False"

    nova_simulacao = models.Simulacao(
        id_solicitacao=simulacao.id_solicitacao,
        valor_simulado=simulacao.valor_simulado,
        prazo_meses=simulacao.prazo_meses,
        taxa_mensal=simulacao.taxa_mensal,
        valor_parcela=valor_parcela,
        valor_total=valor_total,
        parcela_compativel=parcela_compativel,
        data_simulacao=date.today()
    )

    db.add(nova_simulacao)
    db.commit()
    db.refresh(nova_simulacao)

    return nova_simulacao