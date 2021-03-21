import pandas as pd
from preprocessing import preprocessamento, missing
import numpy as np
import matplotlib as plt

pre = preprocessamento.Preprocessamento()

df1, df2, df3, df4, df5 = map(pre.ler_csv, ['imob1.csv', 'imob2.csv',
                                            'imob3.csv', 'imob4.csv',
                                            'imob5.csv'])

lista = [df1, df2, df3, df4, df5]

df3['banheiros'] = df3['suites']
df4['banheiros'] = df4['suites']

for l in lista:
    l.drop(columns='suites', inplace=True)

dataset = pre.concatenar_datasets([df1, df2, df3, df4, df5])
dataset = dataset.iloc[:, 2:]
dataset = pre.ajustar_texto(dataset)
dataset = pre.ajustar_nomes_bairros(dataset)

dataset = missing.imputer_media(dataset, 'quartos')
dataset = missing.imputer_media(dataset, 'banheiros')
dataset = missing.imputer_media(dataset, 'valor')
dataset = missing.imputer_knn(dataset, 'area', 4, 5)
print(dataset.info())

""" def media(dataset, coluna):
    mask1 = dataset[coluna] == 0
    mask2 = dataset[coluna] != 0
    dataset.loc[mask] = dataset.loc[mask2].mean()
    return dataset

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = dataset.iloc[:, 1:5].values
y = dataset.iloc[:, 5].values """
