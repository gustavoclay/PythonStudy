import requests
import json

url = 'https://doe.lula.com.br/api/campaign'

p = requests.get(url)
d = json.loads(p.content)
soma = 0
for doador in d['donors']:
    print(doador['nome'], doador['cpf'], doador['valor'], doador['data_envio'])
    soma += float(doador['valor'])

print(soma)