from requests import get
from bs4 import BeautifulSoup as bs
import re
from model import _nulling as nl
import sql

url = 'http://www.jfimobiliaria.com/index/buscaavancada/finalidade/1/tipo/8/cidade/13/'

link = get(url)
imoveis = bs(link.text, 'html.parser')
bairros = imoveis.find_all(re.compile('h1'))
dormitorios = imoveis.find_all('span', {'class': 'dorm'})
banheiros = imoveis.find_all('span', {'class': 'wc'})
garagens = imoveis.find_all('span', {'class': 'vaga'})
areas = imoveis.find_all('span', {'class': 'area'})
valores = imoveis.find_all('span', {'class': 'pull-left'})


def _recuperar_valores(lista_valores):
    temp, valor = [], []
    for val in lista_valores:
        temp.append(val.text)
    for i in range(1, len(temp)):
        if temp[i] == '':
            pass
        else:
            valor.append(temp[i])
    return valor


s = ''


def _ajustar_valores(lista_valores_recuperados):
    valor_final = []
    for v in lista_valores_recuperados:
        temp = v.split(' ')
        temp = re.findall(r'\d', temp[1][0:7])
        valor_final.append(s.join(temp))
    return valor_final


def _ajustar_areas(lista_areas):
    area_final = []
    for area in lista_areas:
        temp = re.findall(r'\d', area.text)
        area_final.append(s.join(temp))
    return area_final


def _ajustar_textos(lista_texto):
    texto_final = []
    for texto in lista_texto:
        texto_final.append(texto.text)
    return texto_final


def main():
    global areas, valores, bairros, dormitorios, banheiros, garagens
    areas = _ajustar_areas(areas)
    valores = _recuperar_valores(valores)
    valores = _ajustar_valores(valores)

    areas = nl(areas)
    valores = nl(valores)
    suites = [0 for i in range(len(bairros))]

    bairros = _ajustar_textos(bairros)
    dormitorios = _ajustar_textos(dormitorios)
    banheiros = _ajustar_textos(banheiros)
    garagens = _ajustar_textos(garagens)

    con = sql.conectar_db()
    sql.inserir_db(con, 'imob5', bairros, dormitorios,
                   banheiros, suites, garagens, areas, valores)


if __name__ == '__main__':
    main()
