from ..rules.credito import (
    calcular_comprometimento_renda,
    verificar_comprometimento,
    verificar_renda,
    verificar_historico,
    calcular_valor_maximo
)


def realizar_pre_analise(
    renda_mensal: float,
    despesas_mensais: float,
    parcelas_atuais: float,
    historico_pagamentos: str,
    atrasos_ultimos_12m: int
):
    comprometimento = calcular_comprometimento_renda(
        renda_mensal,
        despesas_mensais,
        parcelas_atuais
    )

    renda_ok = verificar_renda(renda_mensal)

    comprometimento_ok = verificar_comprometimento(
        comprometimento
    )

    historico_ok = verificar_historico(
        historico_pagamentos,
        atrasos_ultimos_12m
    )

    valor_maximo = calcular_valor_maximo(
        renda_mensal,
        parcelas_atuais
    )

    motivos = []

    if not renda_ok:
        motivos.append(
            "Renda mensal abaixo do mínimo definido no protótipo."
        )

    if not comprometimento_ok:
        motivos.append(
            "Comprometimento de renda acima do limite definido no protótipo."
        )

    if not historico_ok:
        motivos.append(
            "Histórico de pagamentos não compatível com as regras do protótipo."
        )

    if renda_ok and comprometimento_ok and historico_ok:
        resultado = "aprovado"
        motivo = "Perfil compatível com todas as regras da pré-análise."
    else:
        resultado = "nao_aprovado"
        motivo = " ".join(motivos)

    return {
        "comprometimento_renda": comprometimento,
        "renda_compativel": renda_ok,
        "historico_compativel": historico_ok,
        "valor_maximo_simulado": valor_maximo,
        "resultado": resultado,
        "motivo_resultado": motivo
    }