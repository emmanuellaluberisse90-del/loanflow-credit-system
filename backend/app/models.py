from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from .database import Base
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf_hash = Column(String, nullable=False, unique=True, index=True)
    data_nascimento = Column(Date, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    cidade = Column(String, nullable=False)
    data_cadastro = Column(Date, nullable=False)
    status_cadastro = Column(String, nullable=False)

class PerfilFinanceiro(Base):
    __tablename__ = "perfil_financeiro"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False, index=True)
    renda_mensal = Column(Float, nullable=False)
    tipo_renda = Column(String, nullable=False)
    tempo_renda_meses = Column(Integer, nullable=False)
    outras_rendas = Column(Float, nullable=False)
    despesas_mensais = Column(Float, nullable=False)
    dividas_ativas = Column(Float, nullable=False)
    parcelas_atuais = Column(String, nullable=False)
    historico_pagamentos = Column(String, nullable=False)
    atrasos_ultimos_12m = Column(Integer, nullable=False)

class Solicitacao(Base):
    __tablename__ = "solicitacoes"

    id = Column(Integer, primary_key=True, index=True)

    id_cliente = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False,
        index=True
    )

    data_solicitacao = Column(Date, nullable=False)
    tipo_emprestimo = Column(String, nullable=False)
    valor_solicitado = Column(Float, nullable=False)
    prazo_solicitado_meses = Column(Integer, nullable=False)
    finalidade = Column(String, nullable=False)
    status_solicitacao = Column(String, nullable=False)

class Analise(Base):
    __tablename__ = "analises"

    id = Column(Integer, primary_key=True, index=True)

    id_solicitacao = Column(
        Integer,
        ForeignKey("solicitacoes.id"),
        nullable=False,
        index=True
    )

    identidade_verificada = Column(String, nullable=False)
    cadastro_ativo = Column(String, nullable=False)
    renda_compativel = Column(String, nullable=False)
    historico_compativel = Column(String, nullable=False)
    comprometimento_renda = Column(Float, nullable=False)
    valor_maximo_simulado = Column(Float, nullable=False)
    resultado = Column(String, nullable=False)
    motivo_resultado = Column(String, nullable=False)
    data_analise = Column(Date, nullable=False)

class Simulacao(Base):
    __tablename__ = "simulacoes"

    id = Column(Integer, primary_key=True, index=True)

    id_solicitacao = Column(
        Integer,
        ForeignKey("solicitacoes.id"),
        nullable=False,
        index=True
    )

    valor_simulado = Column(Float, nullable=False)
    prazo_meses = Column(Integer, nullable=False)
    taxa_mensal = Column(Float, nullable=False)
    valor_parcela = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    parcela_compativel = Column(Integer, nullable=False, default=0)
    data_simulacao = Column(Date, nullable=False)

class Agencia(Base):
    __tablename__ = "agencias"

    id = Column(Integer, primary_key=True, index=True)
    nome_agencia = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    status = Column(String, nullable=False)

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)

    id_agencia = Column(
        Integer,
        ForeignKey("agencias.id"),
        nullable=False,
        index=True
    )

    data = Column(Date, nullable=False)
    hora_inicio = Column(String, nullable=False)
    hora_fim = Column(String, nullable=False)
    disponivel = Column(String, nullable=False)

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)

    id_cliente = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False,
        index=True
    )

    id_solicitacao = Column(
        Integer,
        ForeignKey("solicitacoes.id"),
        nullable=False,
        index=True
    )

    id_agencia = Column(
        Integer,
        ForeignKey("agencias.id"),
        nullable=False,
        index=True
    )

    id_horario = Column(
        Integer,
        ForeignKey("horarios.id"),
        nullable=False,
        index=True
    )

    data_agendamento = Column(Date, nullable=False)
    status = Column(String, nullable=False)