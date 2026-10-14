"""Programa principal: executa todas as etapas, uma depois da outra."""
from etapa1_carregar import carregar_dados
from etapa2_resumo import mostrar_resumo
from etapa3_amostra import mostrar_amostra
from etapa4_partidos import calcular_votos_por_partido, mostrar_votos_por_partido
from etapa5_vencedores import calcular_vencedores, mostrar_vencedores
from etapa6_exportar import salvar_csv
# Etapa 1: ler os dados
df = carregar_dados()
# Etapa 2: totais gerais
mostrar_resumo(df)
# Etapa 3: primeiras linhas
mostrar_amostra(df)
# Etapa 4: votos por partido
por_partido = calcular_votos_por_partido(df)
mostrar_votos_por_partido(por_partido)
# Etapa 5: prefeitos eleitos
vencedores = calcular_vencedores(df)
mostrar_vencedores(vencedores)
# Etapa 6: salvar o resultado
salvar_csv(vencedores)