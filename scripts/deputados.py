#!/usr/bin/python3

import json
from dados_abertos_API import dados_abertos_get

deputados = dados_abertos_get('deputados', 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordenarPor=nome')

# Escreve os dados em um arquivo
with open('../dados/deputados.json', 'w') as fp:
    json.dump(deputados, fp, sort_keys=True, indent=4)