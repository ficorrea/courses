# Decision Tree

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('02 - Regressão/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting 
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Predicting with Polynomial
y_pred = regressor.predict(6.5)

# Visualising Decision Tree
plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Decision Tree')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
# Este gráfico não é bom pra visualizar, pois mascara os valores de cada posição


# Para melhor resolução
X_grid = np.arange(min(X), max(X), 0.1)   
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Decision Tree')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()