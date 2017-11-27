#!/usr/bin/python3

import json
from dados_abertos_API import dados_abertos_get

proposicoes = dados_abertos_get('proposicoes', 'https://dadosabertos.camara.leg.br/api/v2/proposicoes')

# Escreve os dados em um arquivo
with open('../dados/proposicoes.json', 'w') as fp:
    json.dump(proposicoes, fp, sort_keys=True, indent=4)