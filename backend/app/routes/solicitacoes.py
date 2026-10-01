from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas


router = APIRouter(
    prefix="/solicitacoes",
    tags=["Solicitações"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.SolicitacaoResponse)
def criar_solicitacao(
    solicitacao: schemas.SolicitacaoCreate,
    db: Session = Depends(get_db)
):
    nova_solicitacao = models.Solicitacao(
        id_cliente=solicitacao.id_cliente,
        data_solicitacao=solicitacao.data_solicitacao,
        tipo_emprestimo=solicitacao.tipo_emprestimo,
        valor_solicitado=solicitacao.valor_solicitado,
        prazo_solicitado_meses=solicitacao.prazo_solicitado_meses,
        finalidade=solicitacao.finalidade,
        status_solicitacao=solicitacao.status_solicitacao
    )

    db.add(nova_solicitacao)
    db.commit()
    db.refresh(nova_solicitacao)

    return nova_solicitacao