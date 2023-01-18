#-*- encoding: utf-8 -*-
import cx_Oracle
import numpy as np

queryFileName='query.txt'
queryTextFile = open("query.txt", "r")
fileData=queryTextFile.read()
queryTextFile.close()

# dados de conexão
connection = cx_Oracle.connect("zabbixmv", "trevo48folhas", "192.168.0.201:1521/prd")

# criação do cursor
cursor = connection.cursor()

# query a ser executada
query = (fileData)

# execução da query
cursor.execute(query)

# recuperando os resultados
results = cursor.fetchall()

# fechando a conexão
connection.close()

# abrindo o arquivo para escrita
with open("output.txt", "w") as file:
    for result in results:
        # escrevendo cada linha no arquivo
        file.write(str(result) + "\n")
