from requests import get
from bs4 import BeautifulSoup as bs
import re
import sql

url_base = 'https://www.jbimobiliaria.com.br/comprar/mg/montes-claros/apartamento/'


def _numero_paginas(url):
    link = get(url)
    quantidade_texto = bs(link.text, 'html.parser')
    quantidade_imoveis = quantidade_texto.find(
        'span', {'class': 'quantidade'}).text.split(' ')
    quantidade_imoveis = int(quantidade_imoveis[0][1:])
    if quantidade_imoveis % 2 == 0:
        return quantidade_imoveis // 12
    else:
        return quantidade_imoveis // 12 + 1


def _urls(quantidade_paginas):
    url_pages = []
    for pagina in quantidade_paginas:
        url_pages.append('pagina-{}/'.format(pagina))
    return url_pages


numero_paginas = _numero_paginas(url_base)
paginas = _urls(range(1, numero_paginas + 1))


def _set_urls(paginas):
    urls = []
    for pagina in paginas:
        urls.append(url_base + '{}'.format(pagina))
    return urls


urls = _set_urls(paginas)

bairros, valores, dormitorios, banheiros, vagas, areas = [], [], [], [], [], []
for url in urls:
    link = get(url)
    imovel_texto = bs(link.text, 'html.parser')
    bairros = bairros + imovel_texto.find_all('h4', {'class': 'bairro'})
    valores = valores + imovel_texto.find_all('div', {'class': 'valor'})
    dormitorios = dormitorios + \
        imovel_texto.find_all('div', {'title': 'Dormitórios'})
    banheiros = banheiros + \
        imovel_texto.find_all('div', {'title': 'Banheiros'})
    vagas = vagas + imovel_texto.find_all('div', {'title': 'Vagas'})
    areas = areas + imovel_texto.find_all('div', {'title': 'Área'})


def _ajustar_valor(lista_valores):
    s = ''
    valor_final = []
    for valor in lista_valores:
        temp = str(valor.contents[1].text.split(' '))
        temp = re.findall(r'\d', temp)
        valor_final.append(s.join(temp[0:6]))
    return valor_final


def _ajustar_area(lista_areas):
    area_final = []
    for area in lista_areas:
        temp = area.text.split('m²')
        area_final.append(temp[0])
    return area_final


def _nulling(lista):
    lista_final = []
    for l in lista:
        if l.text == '-':
            lista_final.append('0')
        else:
            lista_final.append(l.text)
    return lista_final


def _ajustar_textos(lista_texto):
    texto_final = []
    for texto in lista_texto:
        texto_final.append(texto.text)
    return texto_final


def main():
    global valores, areas, dormitorios, banheiros, vagas, bairros
    valores = _ajustar_valor(valores)
    areas = _ajustar_area(areas)

    dormitorios = _nulling(dormitorios)
    banheiros = _nulling(banheiros)
    vagas = _nulling(vagas)
    suites = [0 for i in range(len(bairros))]
    bairros = _ajustar_textos(bairros)

    con = sql.conectar_db()
    sql.inserir_db(con, 'imob2', bairros, dormitorios,
                   banheiros, suites, vagas, areas, valores)


if __name__ == '__main__':
    main()
