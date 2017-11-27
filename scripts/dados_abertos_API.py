#!/usr/bin/python3

import requests
import json


def dados_abertos_get(tipo_dos_dados, url_inicial):
    dados = {}
    proxima_url = url_inicial

    while proxima_url:
        print("Baixando dados dos {} em {}".format(tipo_dos_dados, proxima_url))
        resp = requests.get(proxima_url)

        if resp.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        # Adiciona as novas informacoes no dicionario
        for deputado in resp.json()['dados']:
            dados[deputado['id']] = deputado

        # Encontra a proxima url se tiver
        proxima_url = ''
        for link in resp.json()['links']:
            if link['rel'] == 'next':
                proxima_url = link['href']
                break

    return dados
