import pandas as pd
from sqlalchemy import create_engine
from abstract_etl import AbstractETL
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from modelos.base import Base
from modelos.empregado import Empregado
from modelos.departamento import Departamento
from modelos.dependente import Dependente
from modelos.localizacao import Localizacao
from modelos.projeto import Projeto
from modelos.trabalhaem import TrabalhaEm

# Carregar variáveis do .env
load_dotenv()

class ETL(AbstractETL):
    origem = "E:/Praticando programacao/Projetos/ATV POO/atividade de ap2/tentativa 433/dados.csv"

    def extract(self):
        """
        Método responsável por extrair os dados do arquivo Excel 'empresa_banco_dados.xlsx'.
        """
        try:
            # Caminho para o arquivo (pode ser relativo ou absoluto)
            arquivo_excel = 'empresa_banco_dados2.xlsx'

            # Verifica se o arquivo existe no caminho especificado
            if not os.path.exists(arquivo_excel):
                print(f"Erro: O arquivo '{arquivo_excel}' não foi encontrado.")
                return None

            print(f"Iniciando a extração dos dados do arquivo '{arquivo_excel}'...")

            # Abre o arquivo Excel
            xls = pd.ExcelFile(arquivo_excel)  # Abre o arquivo Excel

            # Inicializa um dicionário para armazenar os dados de cada aba
            dados = {}

            # Itera sobre cada aba e armazena os dados em um DataFrame
            for aba in xls.sheet_names:
                print(f"Carregando dados da aba '{aba}'...")
                df = pd.read_excel(xls, aba)  # Carrega os dados da aba
                dados[aba] = df  # Armazena o DataFrame no dicionário, usando o nome da aba como chave

            # Armazena os dados extraídos no atributo da classe
            self._dados_extraidos = dados
            print("Dados extraídos com sucesso.")

            return dados  # Se precisar retornar, mas geralmente isso já estará em self._dados_extraidos

        except Exception as e:
            print(f"Erro ao extrair dados: {e}")
            return None

    def transform(self, session):
        """Transforma os dados extraídos para as outras tabelas do banco."""
        try:
            dados_transformados = []  # Armazena os dados transformados para posterior carregamento

            for _, row in self._dados_extraidos.iterrows():
                # Verifica ou cria o Departamento
                departamento = session.query(Departamento).filter_by(nome=row['nome_departamento']).first()
                if not departamento:
                    departamento = Departamento(
                        nome=row['nome_departamento'], 
                        numeroEmpregado=row['numero_empregado'], 
                        dataInicio=row['data_inicio_departamento']
                    )
                    session.add(departamento)
                    session.flush()  # Garante que o ID é gerado para uso imediato

                # Verifica ou cria o Empregado
                empregado = session.query(Empregado).filter_by(nss=row['nss_empregado']).first()
                if not empregado:
                    empregado = Empregado(
                        nss=row['nss_empregado'], pnome=row['pnome_empregado'], 
                        mnome=row['mnome_empregado'], snome=row['snome_empregado'],
                        sexo=row['sexo_empregado'], dataNasc=row['data_nascimento_empregado'], 
                        salario=row['salario_empregado'], endereco=row['endereco_empregado'],
                        nssSupervisor=row['nss_supervisor']  # Relacionamento com o próprio empregado (caso haja supervisor)
                    )
                    session.add(empregado)
                    session.flush()  # Garante que o ID é gerado para uso imediato

                # Verifica ou cria o Dependente
                dependente = session.query(Dependente).filter_by(numeroDependente=row['numero_dependente'], nome=row['nome_dependente']).first()
                if not dependente:
                    dependente = Dependente(
                        numeroDependente=row['numero_dependente'], 
                        nome=row['nome_dependente'], 
                        sexo=row['sexo_dependente'],
                        dataNasc=row['data_nasc_dependente'],
                        tipoRelacionamento=row['tipo_relacionamento_dependente']
                    )
                    session.add(dependente)

                # Verifica ou cria a Localizacao
                localizacao = session.query(Localizacao).filter_by(localizacao=row['localizacao']).first()
                if not localizacao:
                    localizacao = Localizacao(localizacao=row['localizacao'])
                    session.add(localizacao)
                
                # Verifica ou cria o Projeto
                projeto = session.query(Projeto).filter_by(nome=row['nome_projeto']).first()
                if not projeto:
                    projeto = Projeto(
                        nome=row['nome_projeto'], 
                        localizacao=row['localizacao_projeto']
                    )
                    session.add(projeto)
                    session.flush()  # Garante que o ID é gerado para uso imediato

                # Associa o Empregado ao Projeto (TrabalhaEm)
                trabalha_em = session.query(TrabalhaEm).filter_by(
                    nssEmpregado=row['nss_empregado'], 
                    numeroProjeto=projeto.numero_Projeto
                ).first()
                if not trabalha_em:
                    trabalha_em = TrabalhaEm(
                        nssEmpregado=row['nss_empregado'], 
                        numeroProjeto=projeto.numero_Projeto, 
                        horas=row['horas_trabalho']
                    )
                    session.add(trabalha_em)

                # Adiciona os dados transformados para o carregamento
                dados_transformados.append(row)

            session.commit()  # Confirma todas as inserções
            self._dados_transformados = pd.DataFrame(dados_transformados)  # Guarda os dados transformados
            print("Dados transformados com sucesso.")
        except Exception as e:
            print(f"Erro ao transformar dados: {e}")
            session.rollback()  # Reverte as operações em caso de erro

    def load(self):
        """Carrega os dados transformados para o destino especificado."""
        try:
            if hasattr(self, '_dados_transformados') and not self._dados_transformados.empty:
                # Construindo a URI de conexão para o SQL Server com as variáveis do .env
                usuario = os.getenv("USUARIO")
                senha = os.getenv("SENHA")
                host = os.getenv("HOST")
                banco_de_dados = os.getenv("BANCO_DE_DADOS")
                
                destino = f"mssql+pyodbc://{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

                # Criando a conexão e carregando os dados
                engine = create_engine(destino)
                self._dados_transformados.to_sql('dados_transformados', con=engine, if_exists='replace', index=False)
                print("Dados carregados com sucesso no banco de dados.")
            else:
                print("Nenhum dado para carregar. Execute primeiro o método 'transform'.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")