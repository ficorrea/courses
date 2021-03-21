import pandas as pd
from preprocessing import preprocessamento, missing
import numpy as np

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
# dataset['valor'] = dataset['valor'].astype(float)

dataset.drop(columns='area', inplace=True)
# dataset.loc[dataset['area'] <= 1,
#             'area'] = dataset.loc[dataset['area'] > 1, 'area'].mean()
dataset.loc[dataset['valor'] == 0,
            'valor'] = dataset.loc[dataset['valor'] != 0, 'valor'].mean()
dataset.loc[dataset['valor'] ==
            2000000, 'valor'] = dataset.loc[dataset['valor'] != 0, 'valor'].mean()
            
dataset = dataset.loc[dataset['bairro'] == 'Ibituruna']

dataset

from sklearn.preprocessing import Imputer
x = dataset.iloc[:, 1:4].values
imp = Imputer(missing_values=0, strategy='mean', axis=0)
x[:, [1, 2]] = imp.fit_transform(x[:, [1, 2]])
y = dataset.iloc[:, 4].values

# x = x[:, 1:].astype(float)
pd.DataFrame(x).info()
pd.DataFrame(y).info()
dataset.info()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)


# x_train = x_train[:, 1:]

import statsmodels.formula.api as sm
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
    temp = np.zeros((225, 5)).astype(int)
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
    print(regressor_OLS.summary())
    return x



pd.DataFrame(x_train).info()
pd.DataFrame(y_train).info()

sl = 0.05
x_train = np.append(arr=np.ones((225, 1)).astype(float),
                    values=x_train, axis=1)
lista = list(range(0, 5))
x_opt = x_train[:, lista]
modelo = back(x_opt, sl, y_train)
modelo = backElimination(x_opt, sl, y_train)
# print(pd.DataFrame(modelo))

