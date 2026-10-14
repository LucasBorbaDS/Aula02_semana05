# Aula 02 - Semana 05

Projeto didático de análise de dados eleitorais desenvolvido em Python. A
aplicação lê os dados de eleições armazenados em CSV, calcula indicadores,
exibe os resultados no terminal e exporta os prefeitos vencedores para um novo
arquivo CSV.

## O que o projeto faz

- carrega os dados de `dados/eleicoes.csv` com `pandas`;
- preserva `zona` e `secao` como texto, mantendo zeros à esquerda;
- exibe um resumo com registros, votos, cidades e candidatos;
- mostra uma amostra dos dados em uma tabela formatada;
- agrupa e ordena os votos por partido;
- identifica o candidato mais votado para prefeito em cada cidade;
- salva os vencedores em `dados/resultado_prefeitos.csv`;
- formata números no padrão brasileiro e usa tabelas e painéis coloridos com
  `rich`.

## Estrutura do projeto

```text
Aula02_semana05/
├── README.md
├── main.py
├── formatacao.py
├── etapa1_carregar.py
├── etapa2_resumo.py
├── etapa3_amostra.py
├── etapa4_partidos.py
├── etapa5_vencedores.py
├── etapa6_exportar.py
├── pyproject.toml
├── uv.lock
├── dados/
│   ├── eleicoes.csv
│   └── resultado_prefeitos.csv
└── src/
    └── aula02_semana05/
        └── __init__.py
```

## Etapas e arquivos principais

- `etapa1_carregar.py`: lê o arquivo de entrada e retorna um `DataFrame`.
- `etapa2_resumo.py`: calcula e exibe os totais gerais.
- `etapa3_amostra.py`: apresenta as primeiras linhas em uma tabela.
- `etapa4_partidos.py`: soma os votos por partido e exibe percentuais.
- `etapa5_vencedores.py`: calcula e exibe o vencedor para prefeito em cada
  cidade.
- `etapa6_exportar.py`: grava a tabela de vencedores no arquivo de saída.
- `formatacao.py`: fornece o console compartilhado e a função `numero_br()`.
- `main.py`: executa todas as etapas na sequência.

## Requisitos

- Python `3.14` ou superior;
- [uv](https://docs.astral.sh/uv/) para criar o ambiente e instalar as
  dependências.

As dependências são declaradas em `pyproject.toml` e incluem `pandas`, `rich`,
`numpy`, `matplotlib`, `openpyxl`, `scikit-learn`, `seaborn` e `jupyterlab`.

## Como executar

Na pasta do projeto, sincronize o ambiente:

```bash
uv sync
```

Para executar o fluxo completo:

```bash
uv run python main.py
```

O comando exibe os resultados no terminal e atualiza o arquivo
`dados/resultado_prefeitos.csv`.

Também é possível executar cada etapa separadamente:

```bash
uv run python etapa1_carregar.py
uv run python etapa2_resumo.py
uv run python etapa3_amostra.py
uv run python etapa4_partidos.py
uv run python etapa5_vencedores.py
uv run python etapa6_exportar.py
```

## Formato dos dados

O arquivo `dados/eleicoes.csv` deve conter, entre outras, as colunas:

`estado`, `cidade`, `zona`, `secao`, `cargo`, `candidato`, `partido` e
`votos`.

O arquivo exportado usa `;` como separador, vírgula como separador decimal e
codificação `utf-8-sig`, facilitando a abertura no Excel em português.

## Observação

Os dados deste projeto são fictícios e têm finalidade exclusivamente
educacional, para praticar leitura, transformação, agregação e apresentação de
dados com Python.
