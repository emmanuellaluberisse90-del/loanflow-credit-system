from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas


router = APIRouter(
    prefix="/perfil-financeiro",
    tags=["Perfil Financeiro"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.PerfilFinanceiroResponse)
def criar_perfil(
    perfil: schemas.PerfilFinanceiroCreate,
    db: Session = Depends(get_db)
):
    novo_perfil = models.PerfilFinanceiro(
        id_cliente=perfil.id_cliente,
        renda_mensal=perfil.renda_mensal,
        tipo_renda=perfil.tipo_renda,
        tempo_renda_meses=perfil.tempo_renda_meses,
        outras_rendas=perfil.outras_rendas,
        despesas_mensais=perfil.despesas_mensais,
        dividas_ativas=perfil.dividas_ativas,
        parcelas_atuais=perfil.parcelas_atuais,
        historico_pagamentos=perfil.historico_pagamentos,
        atrasos_ultimos_12m=perfil.atrasos_ultimos_12m
    )

    db.add(novo_perfil)
    db.commit()
    db.refresh(novo_perfil)

    return novo_perfil