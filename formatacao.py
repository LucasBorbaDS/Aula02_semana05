# Ettapa de formatação de dados, onde os dados são limpos e preparados para análise.

from rich.console import Console

console = Console()

def numerp_br (valor, casas_decimais = 0):
    texto = f"{valor:,.{casas_decimais}f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto