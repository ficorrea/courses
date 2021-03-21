from preprocessing import preprocessamento
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import warnings
warnings.filterwarnings('ignore')

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
coordenadas = pre.ler_csv('bairros_e_coordenadas.csv')
dataset = pre.inserir_coordenadas_geograficas(dataset, coordenadas)

"""Recomendador e busca"""

# Retira linhas que a coluna valor == 0
# e reseta o index
mask = dataset['valor'] != 0
dataset = dataset[mask]


def reset_dataset_index(dataset):
    dataset.reset_index(inplace=True)
    dataset.drop(columns='index', inplace=True)
    return dataset


dataset = reset_dataset_index(dataset)


def knn(vizinhos, X, features):
    neigh = NearestNeighbors(n_neighbors=vizinhos, metric='euclidean').fit(X)
    indices = neigh.kneighbors([features], return_distance=False)
    return list(indices[0])


def coordenadas_geograficas(bairro):
    mask = coordenadas['BAIRROS'] == bairro
    return list(coordenadas.loc[mask, ['LATITUDE', 'LONGITUDE']].values[0])


def bairro_igual_ou_diferente(bairro, opcao):
    if opcao == 0:
        mask = dataset['bairro'] != bairro
    if opcao == 1:
        mask = dataset['bairro'] == bairro
    data = dataset.loc[mask]
    data = reset_dataset_index(data)
    return data, data.iloc[:, 1:].values


def apartamentos(indices, dataset):
    for i in indices:
        apto = dataset.iloc[i]
        print('Bairro {} com {} quarto(s), {} banheiro(s), {} vaga(s) de garagem, área de {}m² e valor de R$ {}.'.format(
            apto['bairro'], apto['quartos'], apto['banheiros'], apto['garagens'], apto['area'], round(apto['valor'], 2)))


def verificar_samples(dataset, bairro):
    return dataset.loc[dataset['bairro'] == bairro, 'bairro'].count()


def retorna_indices(dataset, bairro):
    return list(dataset.loc[dataset['bairro'] == bairro, 'bairro'].index)


def buscar(bairro, quartos, banheiros, garagens, area, valor):
    vizinhos = 10
    data, x = bairro_igual_ou_diferente(bairro, 1)
    quantidade = verificar_samples(data, bairro)
    if quantidade == 0:
        print('Não foram encontrados apartamentos neste bairro.')
        return 0
    elif quantidade < vizinhos:
        indices = retorna_indices(data, bairro)
        print('Apartamentos encontrados: ')
        apartamentos(indices, data)
        return 0
    else:
        pontos = coordenadas_geograficas(bairro)
        features = pontos + [quartos, banheiros, garagens, area, valor]
        indices = knn(vizinhos, x, features)
        print('Apartamentos encontrados: ')
        apartamentos(indices, data)


def recomendar(bairro, quartos, banheiros, garagens, area, valor):
    vizinhos = 10
    data, x = bairro_igual_ou_diferente(bairro, 0)
    pontos = coordenadas_geograficas(bairro)
    features = pontos + [quartos, banheiros, garagens, area, valor]
    indices = knn(vizinhos, x, features)
    print('Você pode se interessar por estes:')
    apartamentos(indices, data)


apto = {'bairro': 'Centro', 'quartos': 3, 'banheiros': 2,
        'garagens': 1, 'area': 80, 'valor': 230000}

buscar(apto['bairro'], apto['quartos'], apto['banheiros'],
       apto['garagens'], apto['area'], apto['valor'])

recomendar(apto['bairro'], apto['quartos'], apto['banheiros'],
           apto['garagens'], apto['area'], apto['valor'])


""" # Avaliação
respostas = pd.read_csv('respostas.csv')


def precisao(respostas):
    valores = []
    for r in respostas:
        valores.append(r/5)
    return valores


def recall(respostas, relevantes):
    valores = []
    for r in respostas:
        valores.append(r/relevantes)
    return valores


def f1_score(precisao, recall):
    score = []
    for p, r in zip(precisao, recall):
        if p == 0 and r == 0:
            score.append(0)
        else:
            score.append(2*p*r/(p+r))
    return score


resp_euclidiana = respostas['Euclidiana'].values
resp_cosseno = respostas['Cosseno'].values

prec_euclidiana = precisao(resp_euclidiana)
rec_euclidiana = recall(resp_euclidiana, 4)
euclidiana = f1_score(prec_euclidiana, rec_euclidiana)
print(pd.DataFrame(prec_euclidiana).mean())
print(pd.DataFrame(rec_euclidiana).mean())
print(pd.DataFrame(euclidiana).mean())

prec_cosseno = precisao(resp_cosseno)
rec_cosseno = recall(resp_cosseno, 3)
cosseno = f1_score(prec_cosseno, rec_cosseno)
print(pd.DataFrame(prec_cosseno).mean())
print(pd.DataFrame(rec_cosseno).mean())
print(pd.DataFrame(cosseno).mean()) """
