"""Etapa 5: descobrir o prefeito eleito em cada cidade."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br
def calcular_vencedores(df):
    # 1. Fica só com as linhas de prefeito (ignora vereadores)
    prefeitos = df[df["cargo"] == "Prefeito"]
    # 2. Soma os votos de cada candidato, juntando todas as seções da cidade
    por_candidato = prefeitos.groupby(
        ["estado", "cidade", "candidato", "partido"], as_index=False
    )["votos"].sum()
    # 3. Calcula o percentual de cada candidato dentro da sua cidade.
    #    transform("sum") coloca, em cada linha, o total de votos da cidade.
    total_da_cidade = por_candidato.groupby("cidade")["votos"].transform("sum")
    por_candidato["percentual"] = (por_candidato["votos"] / total_da_cidade * 100).round(1)
    # 4. Ordena do mais votado para o menos votado
    #    e fica com o primeiro de cada cidade (o vencedor)
    ordenado = por_candidato.sort_values("votos", ascending=False)
    vencedores = ordenado.drop_duplicates("cidade")
    # 5. Ordena por nome da cidade para ficar mais fácil de ler
    return vencedores.sort_values("cidade")
def mostrar_vencedores(vencedores):
    tabela = Table(title="Prefeitos eleitos", header_style="bold cyan")
    tabela.add_column("UF")
    tabela.add_column("Cidade")
    tabela.add_column("Candidato", style="bold")
    tabela.add_column("Partido")
    tabela.add_column("Votos", justify="right")
    tabela.add_column("%", justify="right")
    for _, linha in vencedores.iterrows():
        tabela.add_row(
            linha["estado"],
            linha["cidade"],
            linha["candidato"],
            linha["partido"],
            numero_br(linha["votos"]),
            numero_br(linha["percentual"], 1),
        )
    console.print(tabela)
if __name__ == "__main__":
    df = carregar_dados()
    vencedores = calcular_vencedores(df)
    mostrar_vencedores(vencedores)