# Módulo responsável por carregar os dados eleitorais em um DataFrame.
# Esse arquivo lê o arquivo CSV principal do projeto e prepara os dados para análise.
import pandas as pd

# Caminho do arquivo CSV que contém os dados das eleições.
CAMINHO_CSV = 'eleicoes.csv'


def carregar_dados():
    # Lê o CSV e mantém as colunas de zona e seção como texto para evitar
    # perda de zeros à esquerda e inconsistências em códigos numéricos.
    df = pd.read_csv(CAMINHO_CSV, dtype={"zona": str, "secao": str})
    return df


if __name__ == "__main__":
    # Quando executado diretamente, exibe as primeiras linhas dos dados.
    df = carregar_dados()
    print(df.head())