# Grid Search

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

y_predict = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)

from sklearn.model_selection import GridSearchCV
parametros = [{'C':[1, 10, 100], 'kernel':['linear']},
              {'C':[1, 10, 100], 'kernel':['rbf'], 'gamma':[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]}]
grid_search = GridSearchCV(estimator=classifier, param_grid=parametros, scoring='accuracy', cv=10, n_jobs= -1)
grid_search = grid_search.fit(X_train, y_train)
accuracy = grid_search.best_score_
params = grid_search.best_params_ 