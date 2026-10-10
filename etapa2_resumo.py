from rich.panel import Panel
from rich import console

from etapa1_carregar import carregar_dados
from formatacao import numero_br, console
# Etapa 02 : Resumo dos resultados das eleições
# Função para mostrar o resumo dos resultados das eleições, incluindo o total de registros, votos, cidades e candidatos.
def mostrar_resultados(df):
    total_registros = len(df)
    total_votos = df['votos'].sum()
    total_cidades = df['cidade'].nunique()
    total_candidatos = df['candidato'].nunique()

    texto = (

        f"[bold] Registro [/] : {total_registros}\n"
        f"[bold] Total de Votos [/] : {total_votos}\n"
        f"[bold] Total de Cidades [/] : {total_cidades}\n"
        f"[bold] Total de Candidatos [/] : {total_candidatos}\n"
    )
# Exibe o resumo dos resultados em um painel
    console.print(Panel(texto, title="Resumo dos Resultados", expand=False))
# Executa a função mostrar_resultados se o script for executado diretamente
if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resultados(df)
