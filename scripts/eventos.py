#!/usr/bin/python3

import json
from dados_abertos_API import dados_abertos_get

eventos = dados_abertos_get('eventos', 'https://dadosabertos.camara.leg.br/api/v2/eventos?ordenarPor=id')

# Escreve os dados em um arquivo
with open('../dados/eventos.json', 'w') as fp:
    json.dump(eventos, fp, sort_keys=True, indent=4)