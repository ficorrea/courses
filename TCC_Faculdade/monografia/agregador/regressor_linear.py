import pandas as pd
from preprocessing import preprocessamento, missing
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

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
dataset['valor'] = dataset['valor'].astype(float)


# Outliers
dataset.loc[dataset['area'] >= 300, 'area'] = dataset['area'].mean()
dataset.loc[dataset['valor'] >= 2000000, 'valor'] = dataset['valor'].mean()
dataset.loc[dataset['valor'] < 30000, 'valor'] = dataset['valor'].mean()

# dataset = missing.imputer_media(dataset, 'valor')
dataset = missing.imputer_media_grupo(
    dataset, 'quartos', 'valor', [1, 2, 3, 4, 5])
dataset = missing.imputer_media(dataset, 'quartos')
dataset = missing.imputer_media(dataset, 'banheiros')
dataset = missing.imputer_knn(dataset, 'area', 4, 5)
#dataset = missing.imputer_media_grupo(dataset, 'quartos', 'area', range(1, 6))

m = dataset['quartos'] == 1
m2 = dataset['area'] >= 100.0
m3 = dataset['area'] < 100.0
dataset.loc[m & m2, 'area'] = dataset.loc[m & m3, 'area'].mean()

""" x = dataset.iloc[:, 0:5].values
y = dataset.iloc[:, 5].values """

# data = dataset.iloc[:, 1:5].values

""" from scipy import stats
print(stats.pearsonr(x[:, 4], y)) """

# Cluster
""" from sklearn.cluster import KMeans
w = []
for i in range(1, 11):
    cluster = KMeans(n_clusters=i, random_state=0)
    cluster.fit(data)
    w.append(cluster.inertia_)  # print(indice.labels_)
# plt.plot(range(1, 11), w)
# plt.show()

cluster = KMeans(n_clusters=4, random_state=0)
indices = cluster.fit(data)
ind = pd.DataFrame(indices.labels_)
cluster1 = ind.loc[ind[0] == 0]
cluster2 = ind.loc[ind[0] == 1]
cluster3 = ind.loc[ind[0] == 2]
cluster4 = ind.loc[ind[0] == 3]
a = list(cluster1.index)
b = list(cluster2.index)
c = list(cluster3.index)
d = list(cluster4.index) """


x = dataset.iloc[:, 0:5].values
y = dataset.iloc[:, 5].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label = LabelEncoder()
x[:, 0] = label.fit_transform(x[:, 0])
onehot = OneHotEncoder(categorical_features=[0])
x = onehot.fit_transform(x).toarray()
x = x[:, 1:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

# print(len(x_train), len(x_test))


def back(data, sl, y):
    col = len(data[0])
    for i in range(0, col):
        ols = sm.OLS(y, data).fit()
        vlr = max(ols.pvalues).astype(float)
        if vlr > sl:
            for j in range(0, col - i):
                if ols.pvalues[j].astype(float) == vlr:
                    data = np.delete(data, j, 1)
    print(ols.summary())
    return data


def backElimination(x, SL, y):
    numVars = len(x[0])
    temp = np.zeros((536, 48)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:, j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:, [0, j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print(regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x


""" sl = 0.05
x_train = np.append(arr=np.ones((536, 1)).astype(float),
                    values=x_train, axis=1)
lista = list(range(0, 48))

x_opt = x_train[:, lista]
result = sm.OLS(y_train, x_train).fit()
res = result.rsquared
print(res)
print(result.summary()) """

# modelo = back(x_opt, sl, y_train)
# modelo = backElimination(x_opt, sl, y_train)

""" pd.DataFrame(modelo)

x_train = x_train[:, 1:]
x_train """

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn import metrics


def linear():
    print('Média Validação Cruzada,', 'Desvio-Padrão Validação Cruzada,',
          'Média Erro Absoluto,', 'R²,', 'Variância Explicada')
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    y_predict = regressor.predict(x_test)
    acuracia = cross_val_score(
        regressor, x_train, y_train, cv=10, n_jobs=-1)
    print(acuracia.mean(), ',', acuracia.std(), ',', metrics.mean_absolute_error(y_test, y_predict),
          ',', metrics.r2_score(y_test, y_predict), ',', metrics.explained_variance_score(y_test, y_predict))


metrica()

""" regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_predict = regressor.predict(x_test) """

from sklearn.metrics import r2_score
# print(r2_score(y_test, y_predict))

""" from sklearn.metrics import explained_variance_score
print(explained_variance_score(y_test, y_predict))

from scipy import stats
print(stats.pearsonr(y_test, y_predict)) """

# Gráfico de barra valores reais x preditos
""" ind = np.arange(len(y_test))
larg = 0.3
fig, ax = plt.subplots()
real = ax.bar(ind - larg/2, y_test, larg, color='blue', label='Real')
pred = ax.bar(ind + larg/2, y_predict, larg, color='red', label='Predito')
ax.set_ylabel('Valores')
ax.set_title('Reais x Preditos')
ax.set_xticks(ind)
plt.show() """


def erro_global(real, predito, potencia):
    erro = []
    for r, p in zip(real, predito):
        erro.append((r - p)**potencia)
    return erro


# Gráfico histograma erro global
""" erro = erro_global(y_test, y_predict, 1)
plt.hist(erro)
plt.show()

from sklearn.model_selection import cross_val_score
acuracia = cross_val_score(regressor, x_train, y_train, cv=10, n_jobs=-1)
print(acuracia.mean(), acuracia.std()) """
