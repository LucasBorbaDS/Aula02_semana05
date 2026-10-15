"""Etapa 3: mostrar as primeiras linhas dos dados em uma tabela."""
from rich.table import Table
from etapa1_carregar import carregar_dados
from formatacao import console
def mostrar_amostra(df, linhas=5):
    # Escolhemos só algumas colunas para a tabela caber na tela
    colunas = ["estado", "cidade", "secao", "cargo", "candidato", "partido", "votos"]
    # 1. Cria a tabela vazia
    tabela = Table(title=f"Primeiras {linhas} linhas", header_style="bold cyan")
    # 2. Adiciona o cabeçalho (uma coluna por vez)
    for coluna in colunas:
        tabela.add_column(coluna)
    # 3. Adiciona as linhas. head() pega as primeiras linhas do DataFrame
    for _, linha in df.head(linhas).iterrows():
        # A tabela só aceita texto, por isso o str()
        valores = [str(linha[coluna]) for coluna in colunas]
        tabela.add_row(*valores)
    # 4. Mostra no terminal
    console.print(tabela)
if __name__ == "__main__":
    df = carregar_dados()
    mostrar_amostra(df, linhas=5)
    