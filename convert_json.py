import csv
import json

# nome do arquivo csv
csv_file = 'output.txt'

# nome do arquivo json
json_file = 'dados.json'

# abrindo o arquivo csv
data = []
with open(csv_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# escrevendo o arquivo json
with open(json_file, 'w') as f:
    json.dump(data, f)

print(f'Arquivo {csv_file} convertido para {json_file} com sucesso!')
