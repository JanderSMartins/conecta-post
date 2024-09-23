import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


# Função para conectar ao banco de dados PostgreSQL usando SQLAlchemy
def connect_to_db() :
    try :
        # Substitua pelas suas credenciais e informações de conexão
        engine = create_engine(
            'postgresql://jander:piJDHj4qL7ra@omni-myfinance-sandbox.ckudf0ywkx4n.us-east-1.rds.amazonaws.com:5432/myfinance_sandbox')
        return engine
    except Exception as e :
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Função para ler os dados da tabela do banco de dados
def get_table_data(engine) :
    try :
        query = "SELECT * FROM financial_accounts;"  # Substitua pelo nome da tabela
        df = pd.read_sql(query , engine)
        return df
    except Exception as e :
        st.error(f"Erro ao ler os dados da tabela: {e}")
        return None


# Streamlit App
st.title("Conexão ao PostgreSQL na AWS via Streamlit com SQLAlchemy")
#  alterei
# Conectar ao banco de dados
engine = connect_to_db()

if engine :
    st.success("Conexão estabelecida com sucesso!")

    # Ler os dados da tabela
    df = get_table_data(engine)

    if df is not None :
        st.write("Dados da tabela:")
        st.dataframe(df)  # Exibe a tabela de dados no Streamlit
else :
    st.error("Não foi possível conectar ao banco de dados.")
