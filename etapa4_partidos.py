"""Etapa 4: somar os votos de cada partido."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br
def calcular_votos_por_partido(df):
    # groupby("partido") separa as linhas por partido;
    # ["votos"].sum() soma os votos de cada grupo.
    por_partido = df.groupby("partido")["votos"].sum()
    # Ordena do partido mais votado para o menos votado
    por_partido = por_partido.sort_values(ascending=False)
    return por_partido
def mostrar_votos_por_partido(por_partido):
    total = por_partido.sum()
    tabela = Table(title="Votos por partido", header_style="bold cyan")
    tabela.add_column("Partido")
    tabela.add_column("Votos", justify="right")  # números alinhados à direita
    tabela.add_column("%", justify="right")
    tabela.add_column("Gráfico")
    # items() devolve pares (partido, votos)
    for partido, votos in por_partido.items():
        percentual = votos / total * 100
        # Barra de texto: um bloco "█" a cada 2%
        barra = "█" * round(percentual / 2)
        
        tabela.add_row(
            partido,
            numero_br(votos),
            numero_br(percentual, 1),
            f"[green]{barra}[/]",
        )
    console.print(tabela)

if __name__ == "__main__":
    df = carregar_dados()
    por_partido = calcular_votos_por_partido(df)
    mostrar_votos_por_partido(por_partido)