import streamlit as st
import psycopg2
import pandas as pd
import time

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db() :
    try :
        # Conecte ao banco de dados
        conn = psycopg2.connect(
            host="omni-myfinance-sandbox.ckudf0ywkx4n.us-east-1.rds.amazonaws.com" ,  # ou o endereço do seu servidor PostgreSQL
            database="myfinance_sandbox" ,  # nome do banco de dados
            user="jander" ,  # nome de usuário do PostgreSQL
            password="piJDHj4qL7ra"  # senha do PostgreSQL
        )
        return conn
    except Exception as e :
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Função para ler a tabela do banco de dados
def get_table_data(conn) :
    try :
        query = "SELECT * FROM account_users;"  # Substitua pelo nome da sua tabela
        df = pd.read_sql(query , conn)
        return df
    except Exception as e :
        st.error(f"Erro ao ler a tabela: {e}")
        return None

# Streamlit App
st.title("Conexão ao PostgreSQL via Streamlit")

# Conectar ao banco de dados
conn = connect_to_db()

if conn is not None :
    st.success("Conectado ao banco de dados com sucesso!")

    # Ler os dados da tabela
    df = get_table_data(conn)

    if df is not None :
        st.dataframe(df)  # Exibe a tabela de dados no Streamlit

    # Fechar a conexão
    conn.close()
else :
    st.error("Não foi possível conectar ao banco de dados.")

