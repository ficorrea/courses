# Simple Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('02 - Regressão/Salary_Data.csv')
X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting
y_predict = regressor.predict(X_test)

# Visualing train
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salario x Experiencia (Treino)')
plt.xlabel('Experiencia')
plt.ylabel('Salario')
plt.show()

# Visualing test
plt.scatter(X_test, y_test, color='red')
# Neste trecho não precisa alterar para x_test pois se trata da mesma equação e consequentemente a mesma reta
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salario x Experiencia (Teste)')
plt.xlabel('Experiencia')
plt.ylabel('Salario')
plt.show()
