# Módulo de utilidades para formatar valores numéricos em padrão brasileiro.
# Ele converte números para strings com separação de milhar e vírgula decimal.

from rich.console import Console

# Instância global do console para impressão formatada em terminal.
console = Console()


def numero_br(valor, casas_decimais=0):
    # Converte um número para o formato brasileiro, por exemplo: 1234.5 -> 1.234,5.
    texto = f"{valor:,.{casas_decimais}f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto