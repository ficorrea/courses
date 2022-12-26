""" Métodos utilizados em conjunto pelos scraps 3 e 4 """

from requests import get
from bs4 import BeautifulSoup as bs
import re


def _numero_paginas(url):
    link = get(url)
    quantidade_imoveis = bs(link.text, 'html.parser')
    paginas = quantidade_imoveis.find(
        'p', {'class': 'qntImoveis'}).text.split(' ')
    paginas = int(paginas[0])
    return paginas // 10 + 1


def _urls(quantidade_paginas):
    url_pages = []
    for pagina in quantidade_paginas:
        url_pages.append('page={}&visualizar=0'.format(pagina))
    return url_pages


def _set_urls(url_base, urls):
    links_url = []
    for url in urls:
        links_url.append(url_base + '{}'.format(url))
    return links_url


def _get_apartamentos(urls):
    apartamentos = []
    for url in urls:
        link = get(url)
        imovel_texto = bs(link.text, 'html.parser')
        apartamentos = apartamentos + \
            imovel_texto.find_all('div', {'class': 'bgImovel'})
    return apartamentos


def _recuperar_bairros(lista_apartamentos):
    bairro_final = []
    s = ' '
    for bairro in lista_apartamentos:
        temp = bairro.text.split('-')
        b_temp = temp[1].split(' ')
        c_temp = s.join(b_temp[2:])
        bairro_final.append(c_temp)
    return bairro_final


def _recuperar_features(lista_apartamentos, separador):
    feature_final = []
    for feature in lista_apartamentos:
        temp = feature.text.split(separador)
        f_temp = temp[0]
        feature_final.append(f_temp[-2])
    return feature_final


def _recuperar_valor(lista_apartamentos):
    s = ''
    valor_final = []
    for valor in lista_apartamentos:
        temp = valor.text.split(' ')
        temp = re.findall(r'\d', temp[-5])
        valor_final.append(s.join(temp))
    return valor_final


def _nulling(lista):
    lista_final = []
    for l in lista:
        if l == ' ' or l is None or l == '':
            lista_final.append('0')
        else:
            lista_final.append(l)
    return lista_final
