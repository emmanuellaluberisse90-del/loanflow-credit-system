from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import models, schemas


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ClienteResponse)
def criar_cliente(
    cliente: schemas.ClienteCreate,
    db: Session = Depends(get_db)
):
    novo_cliente = models.Cliente(
        nome=cliente.nome,
        cpf_hash=cliente.cpf_hash,
        data_nascimento=cliente.data_nascimento,
        telefone=cliente.telefone,
        email=cliente.email,
        cidade=cliente.cidade,
        data_cadastro=cliente.data_cadastro,
        status_cadastro=cliente.status_cadastro
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente

@router.get("/", response_model=list[schemas.ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()

    return clientes

@router.get("/{cliente_id}", response_model=schemas.ClienteResponse)
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente