import pandas as pd
import mysql.connector
import psycopg2
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_HOST = os.getenv('MYSQL_HOST') or os.getenv('MYSQL_SERVER')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or os.getenv('MYSQL_PWD')
MYSQL_DB = os.getenv('MYSQL_DB')

POSTGRES_HOST = os.getenv('PG_SERVER')
POSTGRES_USER = os.getenv('PG_USER')
POSTGRES_PASSWORD = os.getenv('PG_PWD')
POSTGRES_DB = os.getenv('PG_DB')

def conectar_mysql():
    conexao = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return conexao

def conectar_pg():
    conexao = psycopg2.connect(
        host = POSTGRES_HOST,
        user = POSTGRES_USER,
        password = POSTGRES_PASSWORD,
        database = POSTGRES_DB
    )
    return conexao

def atualizarDronePol(valor, mes, ano, tabela):

    ano = int(ano)
    mes = int(mes)
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month


    if ano > ano_atual or (ano == ano_atual and mes >= mes_atual):
        return "Data Inválida."
    
    else:
        
        try:
            conn = conectar_mysql()
            cursor = conn.cursor()

            conn_pg = conectar_pg()
            cursor_pg = conn_pg.cursor()

            if tabela == "dronepol_operacoes":
                query_verificar = "SELECT operacoes FROM dronepol_operacoes WHERE mes = %s AND ano = %s"
                query_inserir = "INSERT INTO dronepol_operacoes (operacoes, mes, ano) VALUES (%s, %s, %s)"
            else:
                query_verificar = "SELECT minutos FROM dronepol_minutos WHERE mes = %s AND ano = %s"
                query_inserir = "INSERT INTO dronepol_minutos (minutos, mes, ano) VALUES (%s, %s, %s)"

            cursor.execute(query_verificar, (mes, ano))
            validacao = cursor.fetchone()

            if validacao:
                return "Já existem valores para essa data, por favor, verifique corretamente a data inserida."
            else:
                cursor.execute(query_inserir, (valor, mes, ano))
                conn.commit()
                return "Valores inseridos com sucesso!"
        
        except mysql.connector.Error as e:
            return f"Erro no MySQL: {e}"

        finally:
            cursor.close()
            conn.close()

# atualizarDronePol(10, 12,,)