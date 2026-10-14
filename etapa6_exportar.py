"""Etapa 6: salvar o resultado em um novo arquivo CSV."""
from etapa1_carregar import carregar_dados
from etapa5_vencedores import calcular_vencedores
from formatacao import console
CAMINHO_RESULTADO = "dados/resultado_prefeitos.csv"
def salvar_csv(tabela):
    # to_csv grava a tabela em um arquivo. Os parâmetros deixam o
    # arquivo pronto para abrir no Excel em português:
    #   index=False         -> não grava a numeração das linhas
    #   sep=";"             -> separa as colunas com ponto e vírgula
    #   decimal=","         -> usa vírgula nas casas decimais (41,6)
    #   encoding="utf-8-sig" -> mantém os acentos corretos no Excel
    tabela.to_csv(
        CAMINHO_RESULTADO,
        index=False,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
    )
    console.print(f"Resultado salvo em: {CAMINHO_RESULTADO}")
if __name__ == "__main__":
    df = carregar_dados()
    vencedores = calcular_vencedores(df)
    salvar_csv(vencedores)