import mysql.connector
from datetime import date

dia = date.today()

def conectar_db():
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='imoveis')
    return con

def inserir_db(conector, nome_table, bairros, dormitorios, banheiros, suites, vagas, areas, valores):
    cursor = conector.cursor()
    for bairro, dormitorio, banheiro, suite, vaga, area, valor in zip(bairros, dormitorios, banheiros, suites, vagas, areas, valores):
        cursor.execute("""INSERT INTO {} (dia, bairro, quartos, banheiros, suites, garagens, area, valor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""".format(nome_table),
                        (dia, bairro, dormitorio, banheiro, suite, vaga, area, valor))
        conector.commit()
    conector.close()

