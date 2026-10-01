from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from . import models

from .routes import clientes
from .routes import perfil_financeiro
from .routes import solicitacoes
from .routes import analises
from .routes import simulacoes
from .routes import agencias
from .routes import horarios
from .routes import agendamentos


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="LoanFlow API",
    description="API para pré-análise, simulação e agendamento de crédito",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clientes.router)
app.include_router(perfil_financeiro.router)
app.include_router(solicitacoes.router)
app.include_router(analises.router)
app.include_router(simulacoes.router)
app.include_router(agencias.router)
app.include_router(horarios.router)
app.include_router(agendamentos.router)


@app.get("/")
def home():
    return {
        "sistema": "LoanFlow",
        "status": "online",
        "mensagem": "API funcionando corretamente"
    }