from . import preprocessing
from sklearn.neighbors import NearestNeighbors

""" pre = Preprocessamento()

df1, df2, df3, df4, df5 = map(pre.ler_csv, ['imob1.csv', 'imob2.csv',
                                            'imob3.csv', 'imob4.csv',
                                            'imob5.csv'])
dataset = pre.concatenar_datasets([df1, df2, df3, df4, df5])
dataset = dataset.iloc[:, 2:]
dataset = pre.ajustar_texto(dataset)
dataset = pre.ajustar_nomes_bairros(dataset)
coordenadas = pre.ler_csv('bairros.csv')
dataset = pre.inserir_coordenadas_geograficas(dataset, coordenadas)"""

"""Recomendador e busca"""

"""mask = dataset['valor'] != 0
dataset = dataset[mask]
dataset.reset_index(inplace=True)
dataset.drop(columns='index', inplace=True)

y = dataset.iloc[:, 1:].values


def buscar(bairro, quartos, banheiros, suites, garagens, area, valor):
    mask = coordenadas['BAIRROS'] == bairro
    pontos = list(coordenadas.loc[mask, ['LATITUDE', 'LONGITUDE']].values[0])
    features = pontos + [quartos, banheiros, suites, garagens, area, valor]
    vizinhos = NearestNeighbors(n_neighbors=5, metric='euclidean').fit(y)
    array, indices = vizinhos.kneighbors([features])
    indices = list(indices[0])
    print(dataset.iloc[indices])


buscar('Ibituruna', 2, 3, 0, 2, 0, 150000) """
