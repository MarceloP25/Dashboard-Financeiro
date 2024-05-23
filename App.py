# 1. Importa biblioteca
import pandas as pd
import yfinance as yf
import datetime as dt
import streamlit as st

# Configuração inicial do Streamlit
st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("Dashboard Financeiro")

with st.container():
    st.header("Insira as informações solicitadas abaixo")
    column1, column2, column3 = st.columns(3)
    
    # Lista de ativos populares
    ativos_populares = ["PETR4.SA", "VALE3.SA", "MGLU3.SA", "ITSA4.SA", "AAPL", "GOOGL", "MSFT", "AMZN"]

    with column1:
        ativo_selecionado = st.selectbox("Selecione o ativo", options=ativos_populares)
        ativo_digitado = st.text_input("Ou digite o símbolo do ativo", value="")
    
    with column2:
        data_inicial = st.date_input("Selecione a data inicial", dt.datetime(2000, 1, 1))
    
    with column3:
        data_final = st.date_input("Selecione a data final", dt.datetime.today())

# Determina o ativo a ser usado, priorizando o texto digitado
ativo = ativo_digitado if ativo_digitado else ativo_selecionado

# Converte as datas de data_inicial e data_final para datetime.datetime
data_inicial = dt.datetime.combine(data_inicial, dt.datetime.min.time())
data_final = dt.datetime.combine(data_final, dt.datetime.min.time())

# Verifica se a data final é posterior à data inicial
if data_final <= data_inicial:
    st.error("A data final deve ser posterior à data inicial.")
else:
    # 2. Retornar dados API
    try:
        df = yf.download(ativo, start=data_inicial, end=data_final)
        df.index = df.index.date

        # 3. Criar métricas
        last_update = df.index.max()
        last_cotat = round(df.loc[last_update, "Adj Close"], 2)
        min_cotat = round(df["Adj Close"].min(), 2)
        max_cotat = round(df["Adj Close"].max(), 2)
        first_cotat = round(df.loc[df.index.min(), "Adj Close"], 2)
        delta = round(((last_cotat - first_cotat) / first_cotat) * 100, 2)

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(f"Última atualização - {last_update}", "R$ {:,.2f}".format(last_cotat), f"{delta}%")
            with col2:
                st.metric("Maior cotação do período", "R$ {:,.2f}".format(max_cotat))
            with col3:
                st.metric("Menor cotação do período", "R$ {:,.2f}".format(min_cotat))

        # 4. Apresentar resultado na tela
        with st.container():
            st.area_chart(df[["Adj Close"]])
            st.line_chart(df[["Low", "Adj Close", "High"]])

    except Exception as e:
        st.error(f"Erro ao buscar dados para o ativo {ativo}: {e}")
