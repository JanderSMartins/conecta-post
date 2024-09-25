import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

import streamlit as st

# Definir as funções para cada página
def pagina_inicial():
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial!")

def pagina_banco():
    st.title("Conexão com Financeiro")
    st.write("Aqui você pode conectar ao Financeiro e visualizar os dados.")
    # Código de conexão com Banco vai aqui (por exemplo, o que você já criou)

def pagina_sobre():
    st.title("Sobre")
    st.write("Esta é uma aplicação Streamlit com múltiplas páginas.")

# Barra lateral para selecionar as páginas
st.sidebar.title("Menu")
pagina_selecionada = st.sidebar.selectbox("Selecione uma opção", ["Página Inicial", "Conectar ao Financeiro", "Sobre"])

# Exibir a página selecionada
if pagina_selecionada == "Página Inicial":
    pagina_inicial()
elif pagina_selecionada == "Conectar ao Financeiro":
    pagina_banco()
elif pagina_selecionada == "Sobre":
    pagina_sobre()

# Função para conectar ao banco de dados PostgreSQL usando SQLAlchemy
def connect_to_db():
    try:
        engine = create_engine(
            'postgresql://jander:piJDHj4qL7ra@omni-myfinance-sandbox.ckudf0ywkx4n.us-east-1.rds.amazonaws.com:5432/myfinance_sandbox')
        if engine:
            st.success("Conexão estabelecida com sucesso!")
        else:
            st.error("Não foi possível conectar ao banco de dados.")
        return engine
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None
#
# Função para ler os dados da tabela do banco de dados
def get_table_data(df):
    try:
        query = "SELECT  type, amount FROM financial_accounts;"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao ler os dados da tabela: {e}")
        return None

engine = connect_to_db()

if pagina_selecionada == 'Conectar ao Financeiro':
    if engine :
        df = get_table_data(engine)
        if df is not None :
            st.write("Dados da tabela financial_accounts:")
            st.dataframe(df)  # Exibe os dados em formato de tabela no Streamlit
            st.metric(label="Total Amount" , value=sum(df['amount']))
        else :
            st.error("Não foi possível obter os dados da tabela.")
    else :
        st.error("Não foi possível conectar ao banco de dados.")

