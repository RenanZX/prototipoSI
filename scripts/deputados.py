#!/usr/bin/python3

import json
from dados_abertos_API import dados_abertos_get

deputados = dados_abertos_get('deputados', 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordenarPor=nome')

# Escreve os dados em um arquivo
with open('../dados/deputados.json', 'w') as fp:
    json.dump(deputados, fp, sort_keys=True, indent=4)

# import requests
# import json

# dados = {}
# next_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordenarPor=nome'

# while next_url:
#     print("Baixando dados dos deputados em {}".format(next_url))
#     resp = requests.get(next_url)

#     if resp.status_code != 200:
#         raise ApiError('GET /tasks/ {}'.format(resp.status_code))

#     # Adiciona as novas informacoes no dicionario
#     for deputado in resp.json()['dados']:
#         dados[deputado['nome']] = deputado

#     # Encontra a proxima url se tiver
#     next_url = ''
#     for link in resp.json()['links']:
#         if link['rel'] == 'next':
#             next_url = link['href']
#             break


# # Escreve os dados em um arquivo
# with open('../dados/deputados.json', 'w') as fp:
#     json.dump(dados, fp, sort_keys=True, indent=4)
