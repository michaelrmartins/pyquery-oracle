import csv
import sys
import cx_Oracle

queryFileName='query.txt'
queryTextFile = open("query.txt", "r")
fileData=queryTextFile.read()
queryTextFile.close()

db = cx_Oracle.connect("zabbixmv", "trevo48folhas", "192.168.0.201:1521/prd")
SQL = (fileData)
print(SQL)
cursor = db.cursor()
f = open("dual.csv", "w")
writer = csv.writer(f, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
r = cursor.execute(SQL)

#this takes the column names
col_names = [row[0] for row in cursor.description]
writer.writerow(col_names)

for row in cursor:
   writer.writerow(row)
f.close()