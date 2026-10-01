from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models


router = APIRouter(
    prefix="/agencias",
    tags=["Agências"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def criar_agencia(
    nome_agencia: str,
    cidade: str,
    endereco: str,
    status: str,
    db: Session = Depends(get_db)
):
    nova_agencia = models.Agencia(
        nome_agencia=nome_agencia,
        cidade=cidade,
        endereco=endereco,
        status=status
    )

    db.add(nova_agencia)
    db.commit()
    db.refresh(nova_agencia)

    return nova_agencia

@router.get("/")
def listar_agencias(
    db: Session = Depends(get_db)
):
    return db.query(models.Agencia).filter(
        models.Agencia.status == "ativa"
    ).all()