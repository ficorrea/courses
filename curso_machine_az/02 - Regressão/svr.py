# SVR
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('02 - Regressão/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# No caso do SVR é necessário efetuar o scaler, pq ele não implementa
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
y = np.ravel(sc.fit_transform(y.reshape(-1, 1))) # necessário pq os métodos só funcionam com matriz

s = StandardScaler()
y = np.ravel(s.fit_transform(y.reshape(-1, 1)))
# Deu resultado igual ao do curso usando escalers separados

# Fitting 
from sklearn.svm import SVR
regressor = SVR(kernel='rbf') # Definir o kernel
regressor.fit(X, y)

# Predicting with Polynomial
y_pred = s.inverse_transform(regressor.predict(sc.transform(np.array([[6.5]]))))

# Visualising SVR
plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('SVR')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Para melhor resolução
X_grid = np.arange(min(X), max(X), 0.1)   
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('SVR')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()
