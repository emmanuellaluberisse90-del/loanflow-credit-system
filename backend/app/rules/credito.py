def calcular_comprometimento_renda(
    renda_mensal: float,
    despesas_mensais: float,
    parcelas_atuais: float
):
    comprometimento = (
        despesas_mensais + parcelas_atuais
    ) / renda_mensal

    return comprometimento

def verificar_comprometimento(
    comprometimento: float,
    limite: float = 0.30
):
    return comprometimento <= limite

def verificar_renda(
    renda_mensal: float,
    renda_minima: float = 2000
):
    return renda_mensal >= renda_minima

def verificar_historico(
    historico_pagamentos: str,
    atrasos_ultimos_12m: int
):
    historico_ok = historico_pagamentos.lower() in [
        "bom",
        "regular"
    ]

    atrasos_ok = atrasos_ultimos_12m <= 2

    return historico_ok and atrasos_ok

def calcular_valor_maximo(
    renda_mensal: float,
    parcelas_atuais: float,
    percentual_maximo: float = 0.30
):
    capacidade_nova_parcela = (
        renda_mensal * percentual_maximo
        - parcelas_atuais
    )

    if capacidade_nova_parcela <= 0:
        return 0

    return capacidade_nova_parcela