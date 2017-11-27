#!/usr/bin/python3

import json
from dados_abertos_API import dados_abertos_get

orgaos = dados_abertos_get('orgaos', 'https://dadosabertos.camara.leg.br/api/v2/orgaos?ordenarPor=ideComissao')

# Escreve os dados em um arquivo
with open('../dados/orgaos.json', 'w') as fp:
    json.dump(orgaos, fp, sort_keys=True, indent=4)
