def calcular_parcela(
    valor: float,
    prazo_meses: int,
    taxa_mensal: float
):
    taxa = taxa_mensal / 100

    if taxa == 0:
        parcela = valor / prazo_meses
    else:
        parcela = (
            valor * taxa * (1 + taxa) ** prazo_meses
        ) / (
            (1 + taxa) ** prazo_meses - 1
        )

    return round(parcela, 2)

def calcular_valor_total(
    valor_parcela: float,
    prazo_meses: int
):
    return round(
        valor_parcela * prazo_meses,
        2
    )

def verificar_capacidade_parcela(
    valor_parcela: float,
    parcela_maxima: float
):
    return valor_parcela <= parcela_maxima