"""Etapa 1: ler o arquivo CSV com os dados da eleição."""
import pandas as pd
# Caminho do arquivo, a partir da pasta do projeto
CAMINHO_CSV = "dados/eleicoes.csv"
def carregar_dados():
    # read_csv lê o arquivo e devolve uma tabela (DataFrame).
    # "zona" e "secao" são lidas como texto (str) para não perder
    # os zeros à esquerda: "005" continuaria "005", e não 5.
    df = pd.read_csv(CAMINHO_CSV, dtype={"zona": str, "secao": str})
    return df
# Este bloco só roda quando executamos ESTE arquivo diretamente.
# Quando o main.py importa a função, ele é ignorado.
if __name__ == "__main__":
    df = carregar_dados()
    print(f"{len(df)} registros carregados")
    print(df.head())