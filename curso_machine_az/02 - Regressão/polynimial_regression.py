# Polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('02 - Regressão/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Não necessário split, teste e treino pq a quantidade de dados pe pequena

# Fitting Linear
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # Verificar e definir o grau do polinomial
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising Linear Regression
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('v ou F (Linear)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualising Polynomial Regression
X_grid = np.arange(min(X), max(X), 0.1)   # Para uma curvatura melhor da curva do gráfico
X_grid = X_grid.reshape((len(X_grid), 1)) # pois o polinômio é feito com mais pontos
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(X_poly), color='blue')
plt.title('v ou F (Polynomial)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Predicting with Linear
lin_reg.predict(6.5)

# Predicting with Polynimial
lin_reg_2.predict(poly_reg.fit_transform(6.5))

