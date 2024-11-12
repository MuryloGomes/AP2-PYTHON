import pandas as pd
import pyodbc
from sqlalchemy import create_engine, inspect

# Configurações de conexão
usuario = "ALLAN_GABRIELPC\\allan"
servidor = "ALLAN_GABRIELPC\\SQLTROVATO"
banco_de_dados = "Empresa_AP2"
driver = "ODBC Driver 17 for SQL Server"
origem = "C:/Users/allan/OneDrive/Documentos/MeuProjetos/AP2-PYTHON/empresa_banco_dados.xlsx"

# Cria a conexão com o banco de dados
try:
    conn_str = f"mssql+pyodbc://{usuario}@{servidor}/{banco_de_dados}?driver={driver}&trusted_connection=yes"
    engine = create_engine(conn_str)
    connection = engine.connect()
    print("Conexão com o banco de dados bem-sucedida.")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Função para carregar cada aba do Excel como uma tabela no banco de dados
def carregar_aba_no_banco(aba_nome, df):
    # Tranforma colunas para o tipo correto se necessário
    print(f"Transformando dados da aba '{aba_nome}'...")
    # Aplica transformações necessárias
    # Você pode especificar transformações adicionais para cada aba aqui, se necessário
    
    try:
        # Carrega os dados no banco de dados
        df.to_sql(aba_nome, con=engine, if_exists='replace', index=False)
        print(f"Dados da aba '{aba_nome}' carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar os dados da aba '{aba_nome}': {e}")

# Lê todas as abas do Excel
try:
    xls = pd.ExcelFile(origem)
    for aba_nome in xls.sheet_names:
        df = pd.read_excel(xls, aba_nome)
        if not df.empty:
            print(f"Dados extraídos com sucesso da aba '{aba_nome}'.")
            carregar_aba_no_banco(aba_nome, df)
        else:
            print(f"A aba '{aba_nome}' está vazia.")
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
finally:
    connection.close()
    print("Conexão com o banco de dados encerrada.")
