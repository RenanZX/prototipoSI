#!/usr/bin/python3

import requests
import json


def dados_abertos_get(tipo_dos_dados, url_inicial):
    dados = {}
    proxima_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordenarPor=nome'

    while proxima_url:
        print("Baixando dados dos deputados em {}".format(proxima_url))
        resp = requests.get(proxima_url)

        if resp.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        # Adiciona as novas informacoes no dicionario
        for deputado in resp.json()['dados']:
            dados[deputado['nome']] = deputado

        # Encontra a proxima url se tiver
        proxima_url = ''
        for link in resp.json()['links']:
            if link['rel'] == 'next':
                proxima_url = link['href']
                break

    return dados
