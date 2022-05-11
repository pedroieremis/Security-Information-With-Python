import json
from urllib.request import urlopen

dados_filtados = []

url = 'https://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)


dados_filtados.append('INFORMAÇÕES SUAS:')
dados_filtados.append('IP EXTERNO: '+dados['ip'])
dados_filtados.append('HOST: '+dados['hostname'])
dados_filtados.append('PAÍS: '+dados['country'])
dados_filtados.append('ESTADO: '+dados['region'])
dados_filtados.append('CIDADE: '+dados['city'])

dados_filtados.append('\nINFORMAÇÕES DO SEU FORNECEDOR:')
dados_filtados.append('PROVEDOR: '+dados['org'])
dados_filtados.append('LOCALIZAÇÃO PROVEDOR: '+dados['timezone'])

print()
for i in dados_filtados:
    print(i)