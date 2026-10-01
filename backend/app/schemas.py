from datetime import date
from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    nome: str
    cpf_hash: str
    data_nascimento: date
    telefone: str
    email: EmailStr
    cidade: str
    data_cadastro: date
    status_cadastro: str


class ClienteCreate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class PerfilFinanceiroBase(BaseModel):
    id_cliente: int
    renda_mensal: float
    tipo_renda: str
    tempo_renda_meses: int
    outras_rendas: float
    despesas_mensais: float
    dividas_ativas: float
    parcelas_atuais: str
    historico_pagamentos: str
    atrasos_ultimos_12m: int


class PerfilFinanceiroCreate(PerfilFinanceiroBase):
    pass


class PerfilFinanceiroResponse(PerfilFinanceiroBase):
    id: int

    class Config:
        from_attributes = True

class SolicitacaoBase(BaseModel):
    id_cliente: int
    data_solicitacao: date
    tipo_emprestimo: str
    valor_solicitado: float
    prazo_solicitado_meses: int
    finalidade: str
    status_solicitacao: str


class SolicitacaoCreate(SolicitacaoBase):
    pass


class SolicitacaoResponse(SolicitacaoBase):
    id: int

    class Config:
        from_attributes = True

class AnaliseBase(BaseModel):
    id_solicitacao: int
    identidade_verificada: str
    cadastro_ativo: str
    renda_compativel: str
    historico_compativel: str
    comprometimento_renda: float
    valor_maximo_simulado: float
    resultado: str
    motivo_resultado: str
    data_analise: date


class AnaliseCreate(AnaliseBase):
    pass


class AnaliseResponse(AnaliseBase):
    id: int

    class Config:
        from_attributes = True

class SimulacaoBase(BaseModel):
    id_solicitacao: int
    valor_simulado: float
    prazo_meses: int
    taxa_mensal: float
    valor_parcela: float
    valor_total: float
    parcela_compativel: bool
    data_simulacao: date


class SimulacaoCreate(BaseModel):
    id_solicitacao: int
    valor_simulado: float
    prazo_meses: int
    taxa_mensal: float


class SimulacaoResponse(SimulacaoBase):
    id: int

    class Config:
        from_attributes = True