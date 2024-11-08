from etl.abstract_etl import AbstractETL
import pandas as pd  # Importando pandas
from sqlalchemy import create_engine  # Importando create_engine de sqlalchemy
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class ETL(AbstractETL):
    # TODO: defina aqui sua classe ETL
    pass

    def extract(self):
        try:
            self._dados_extraidos = pd.read_excel(self.origem)
            print(f"Dados extraídos com sucesso de {self.origem}")
        except Exception as e:
            print(f"Erro ao extrair dados: {e}")
            self._dados_extraidos = None

    def transform(self):
        if self._dados_extraidos is not None:
            try:
                # Exemplo de transformação: Limpeza de dados (remover linhas com valores nulos)
                self._dados_transformados = self._dados_extraidos.dropna(axis=0, how='any')
                
                # Exemplo de transformação: Renomear as colunas para um formato mais adequado
                self._dados_transformados.columns = [col.strip().lower().replace(" ", "_") for col in self._dados_transformados.columns]
                
                print("Dados transformados com sucesso.")
            except Exception as e:
                print(f"Erro ao transformar os dados: {e}")
                self._dados_transformados = None
        else:
            print("Nenhum dado extraído para transformação.")
            self._dados_transformados = None

    def load(self):
        if self._dados_transformados is not None:
            try:
                # Usar SQLAlchemy para criar uma conexão com o banco de dados
                engine = create_engine(self.destino)
                
                # Carregar os dados no banco de dados (se a tabela já existir, ela será substituída)
                self._dados_transformados.to_sql('tabela_destino', con=engine, if_exists='replace', index=False)
                
                print("Dados carregados com sucesso no destino.")
            except Exception as e:
                print(f"Erro ao carregar os dados: {e}")
        else:
            print("Nenhum dado transformado para carregar.")
