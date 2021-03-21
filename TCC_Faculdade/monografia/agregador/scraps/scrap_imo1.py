# tirei o coding
from requests import get
from bs4 import BeautifulSoup as bs
import re
import sql

url_base = 'http://www.jairamintas.com.br/imoveis/a-venda/apartamento'


def _quantidade_paginas(url):
    link = get(url)
    qtd = bs(link.text, 'html.parser')
    qtd_texto = qtd.find('span', {'class': 'h-money'}).text
    qtd_texto = int(qtd_texto)
    if qtd_texto % 12 != 0:
        pages = qtd_texto // 12 + 1
    else:
        pages = qtd_texto // 12
    return pages


def _urls(quantidade_paginas, url_base):
    pages = []
    for i in range(1, quantidade_paginas + 1):
        pages.append(url_base + '?pagina={}'.format(i))
    return pages


quantidade = _quantidade_paginas(url_base)
urls = _urls(quantidade, url_base)

bairros, features, valores = [], [], []
for url in urls:
    link = get(url)
    imovel = bs(link.text, 'html.parser')
    bairros = bairros + imovel.find_all('h2', {'class': 'card-title'})
    features = features + imovel.find_all('div', {'class': 'values'})
    valores = valores + \
        imovel.find_all('div', {'class': 'col-sm-12 col-lg-6 box-align'})


def _recuperar_valores(lista_valores):
    valores = []
    for valor in lista_valores:
        temp = valor.text.split('R$')
        if temp[0] != '':
            valores.append('0')
        else:
            valores.append(temp[1][0:9])
    return valores


s = ''


def _ajustar_valores(lista_valores_recuperados):
    valores = []
    for valor in lista_valores_recuperados:
        temp = re.findall(r'\d|null', valor)
        valores.append(s.join(temp))
    return valores


def _recuperar_features(lista_features, separador, profundidade_busca, tamanho_resultado):
    feature_final = []
    for feature in lista_features:
        temp = feature.text.split(separador)
        f_temp = temp[0]
        temp = re.findall(r'^M²|\d|,', f_temp[profundidade_busca:])
        if temp == [] or len(temp) == tamanho_resultado:
            feature_final.append('0')
        else:
            feature_final.append(s.join(temp))
    return feature_final


def _ajustar_textos(lista_texto):
    texto_final = []
    for texto in lista_texto:
        texto_final.append(texto.text)
    return texto_final


def _ajustar_decimal(lista):
    lista_final = []
    for numero in lista:
        lista_final.append(numero.replace(',', '.'))
    return lista_final


def main():
    global bairros
    global valores
    dormitorios = _recuperar_features(features, 'dorm', -1, 0)
    banheiros = _recuperar_features(features, 'banheiro', -1, 0)
    suites = _recuperar_features(features, 'suítes', -1, 0)
    vagas = _recuperar_features(features, 'vaga', -1, 0)
    areas = _recuperar_features(features, 'm²', -6, 1)
    areas = _ajustar_decimal(areas)
    valores = _recuperar_valores(valores)
    valores = _ajustar_valores(valores)
    bairros = _ajustar_textos(bairros)

    con = sql.conectar_db()
    sql.inserir_db(con, 'imob1', bairros, dormitorios,
                   banheiros, suites, vagas, areas, valores)


if __name__ == '__main__':
    main()
