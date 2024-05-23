# Dashboard-Financeiro
Dashboard Financeiro com Streamlit

Este repositório contém um projeto de Dashboard Financeiro desenvolvido com Python e Streamlit. O objetivo deste dashboard é permitir a visualização e análise de dados financeiros de ativos disponíveis na API do Yahoo Finance, utilizando gráficos e métricas de desempenho.

Funcionalidades
  - Seleção de ativos populares ou inserção manual de qualquer símbolo de ativo.
  - Escolha de data inicial e final para análise sem restrições temporais.
  - Exibição de métricas financeiras:
  - Última cotação ajustada.
  - Maior cotação do período.
  - Menor cotação do período.
  - Variação percentual desde a primeira cotação do período.
  - Gráficos interativos de área e linha para visualização dos preços do ativo ao longo do tempo.

Instalação
Para executar este projeto, você precisará instalar as seguintes bibliotecas Python. Recomendamos o uso de um ambiente virtual (virtualenv) para gerenciar as dependências.

Passo 1: Criar e ativar um ambiente virtual

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Passo 2: Instalar as dependências

pip install streamlit pandas yfinance


Uso
Executar o Dashboard

Para iniciar o dashboard, execute o seguinte comando no terminal:

streamlit run app.py

![Dashboard Financeiro_page-0001](https://github.com/MarceloP25/Dashboard-Financeiro/assets/84405833/0874a403-05f2-4110-850f-f915760ccac2)
