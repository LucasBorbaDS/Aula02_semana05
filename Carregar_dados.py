#Etapa 01 : Ler o arquivo CSV com os dados das eleições


import pandas as pd

CAMINHO_CSV = 'eleicoes.csv'

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype = {"zona": str, "secao": str})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())