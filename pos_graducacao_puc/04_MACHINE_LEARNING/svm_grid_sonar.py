# -*- coding: utf-8 -*-
"""
svm_sonar.py: Avaliação da performance de classificadores lineares SVM e regressão logística.

Avaliar a performance da classificação da base de dados sonar com os métodos de 
classificação por classificadores lineares.

@author: Prof. Hugo de Paula
@contact: hugo@pucminas.br

@date	  22 Outubro 2017
@version 1.0"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
import numpy as np


np.set_printoptions(precision=2)

# Carrega a base de dados sonar.
sonar = pd.read_excel('../Datasets/sonar.xlsx', sheetname=0) 

X = sonar.iloc[:,0:(sonar.shape[1] - 1)]

le = LabelEncoder()
y = le.fit_transform(sonar.iloc[:,(sonar.shape[1] - 1)])

class_names = le.classes_


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


# Grid Search
# Seleciona os parâmetros da SVM que deseja testar
params = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]}, 
          {'kernel': ['linear'],  'C': [1, 10, 100, 1000]}
         ]

# Executa grid search com cross validation
svmc = GridSearchCV(svm.SVC(C=1), params, cv=5, scoring='precision')
svmc.fit(X_train, y_train)
y_pred = svmc.predict(X_test)


print("\nClassificado usando SVM com GridSearch")
print("Os melhores parâmetros encontrados pelo GrisSearch:")
print(svmc.best_params_,'\n')

print(classification_report(y_test, y_pred, target_names=class_names))


# Calcula a matriz de confusão
cnf_matrix = confusion_matrix(y_test, y_pred)
print(cnf_matrix)


# Regressao logística
print("---------------------------------------")
print("Regressão logística")

lreg = LogisticRegression().fit(X_train, y_train)

y_pred = lreg.predict(X_test)

# Avaliacao
print("Acurácia da base de treinamento: {:.2f}".format(lreg.score(X_train, y_train)))
print("Acurácia da base de teste: {:.2f}".format(lreg.score(X_test, y_test)))
print("Regressão Logística: w: {}  b: {}".format(lreg.coef_, lreg.intercept_))
print("Número de atributos usados: {}".format(np.sum(lreg.coef_ != 0)))
print(classification_report(y_test, y_pred, target_names=class_names))

cnf_matrix = confusion_matrix(y_test, y_pred)
print(cnf_matrix)









