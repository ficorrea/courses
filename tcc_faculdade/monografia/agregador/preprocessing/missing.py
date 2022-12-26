import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.neighbors import NearestNeighbors


def missing_values(x, colunas=0):
    imp = Imputer(missing_values=0, strategy='mean', axis=0)
    x[:, colunas] = imp.fit_transform(x[:, colunas])
    return x


def imputer_media(dataset, coluna):
    mask1 = dataset[coluna] == 0
    mask2 = dataset[coluna] != 0
    dataset.loc[mask1, coluna] = dataset.loc[mask2, coluna].mean()
    return dataset


def imputer_mediana(dataset, coluna):
    mask1 = dataset[coluna] == 0
    mask2 = dataset[coluna] != 0
    dataset.loc[mask1, coluna] = dataset.loc[mask2, coluna].median()
    return dataset


def imputer_media_grupo(dataset, coluna_principal, coluna_imputer, quantidade):
    for q in quantidade:
        mask = dataset[coluna_principal] == q
        mask2 = dataset[coluna_imputer] != 0
        mask3 = dataset[coluna_imputer] == 0
        dataset.loc[mask & mask3, coluna_imputer] = \
            dataset.loc[mask & mask2, coluna_imputer].mean()
    return dataset


def retorna_lista(lista_temp, lista_original):
    lista = []
    for l in lista_temp:
        lista.append(lista_original[l])
    return lista


def imputer_knn(dataset, coluna, numero_coluna, vizinhos):
    data_valor_zero = list(dataset.loc[dataset[coluna] <= 9].index)
    data_valor = list(dataset.loc[dataset[coluna] > 9].index)
    neigh = NearestNeighbors(
        n_neighbors=vizinhos, metric='euclidean').fit(dataset.iloc[data_valor, 3:8].values)
    for posicao in data_valor_zero:
        indices = neigh.kneighbors(
            dataset.iloc[[posicao], 3:8].values, return_distance=False)
        indices = retorna_lista(indices[0], data_valor)
        dataset.iloc[posicao, numero_coluna] = dataset.iloc[indices,
                                                            numero_coluna].mean()
    return dataset
