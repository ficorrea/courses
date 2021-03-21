import model as md
import sql

url_base = 'http://www.masterimoveis.com.br/listagem.aspx? \
                    pretensao=1&tipo=2&cidade2=270&order=11&'

url_search_qtd_imoveis = 'page=1&visualizar=0'

quantidade_links = md._numero_paginas(
    url_base + '{}'.format(url_search_qtd_imoveis))
links = md._urls(range(1, quantidade_links + 1))
urls = md._set_urls(url_base, links)

apartamentos = md._get_apartamentos(urls)


def main():
    global apartamentos
    bairros = md._recuperar_bairros(apartamentos)
    suites = md._recuperar_features(apartamentos, 'suíte(s)')
    dormitorios = md._recuperar_features(apartamentos, 'dorms(s)')
    garagens = md._recuperar_features(apartamentos, 'vaga(s)')
    valores = md._recuperar_valor(apartamentos)

    suites = md._nulling(suites)
    dormitorios = md._nulling(dormitorios)
    garagens = md._nulling(garagens)
    valores = md._nulling(valores)
    banheiros = [0 for i in range(len(bairros))]
    areas = [0 for i in range(len(bairros))]

    con = sql.conectar_db()
    sql.inserir_db(con, 'imob3', bairros, dormitorios,
                   banheiros, suites, garagens, areas, valores)


if __name__ == '__main__':
    main()
