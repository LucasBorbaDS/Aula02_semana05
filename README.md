# Aula 02 - Semana 05

Projeto de análise de dados eleitorais realizado em Python. O objetivo é carregar um arquivo CSV com informações de eleições, realizar uma formatação básica dos dados e exibir um resumo geral dos resultados em terminal.

## Descrição

Este projeto demonstra o uso de:

- leitura de dados com `pandas`
- organização de scripts separados por etapa
- formatação de valores numéricos em padrão brasileiro
- apresentação de indicadores em painel visual com `rich`

## Estrutura do projeto

```text
Aula02_semana05/
├── README.md
├── eleicoes.csv
├── etapa1_carregar.py
├── etapa2_resumo.py
├── formatacao.py
├── pyproject.toml
├── uv.lock
└── src/
    └── aula02_semana05/
        └── __init__.py
```

## Arquivos principais

- `etapa1_carregar.py`: carrega o CSV de eleições e mantém as colunas `zona` e `secao` como texto.
- `formatacao.py`: contém a função `numero_br()`, responsável por formatar valores numéricos em padrão brasileiro.
- `etapa2_resumo.py`: calcula o resumo geral dos dados, como total de registros, votos, cidades e candidatos.

## Requisitos

O projeto depende de bibliotecas Python como:

- `pandas`
- `rich`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

O ambiente pode ser configurado com `uv` ou com um ambiente virtual Python padrão.

## Como executar

1. Acesse a pasta do projeto:

```bash
cd Aula02_semana05
```

2. Instale as dependências:

```bash
uv sync
```

ou, se preferir usar pip:

```bash
pip install -r requirements.txt
```

3. Execute o carregamento dos dados:

```bash
python etapa1_carregar.py
```

4. Execute o resumo dos resultados:

```bash
python etapa2_resumo.py
```

## Exemplo de saída

O script `etapa2_resumo.py` exibe um painel no terminal com informações como:

- total de registros
- total de votos
- total de cidades
- total de candidatos

## Observações

Este é um projeto didático para praticar manipulação e apresentação de dados em Python, com foco em leitura, resumo e visualização básica em terminal.
