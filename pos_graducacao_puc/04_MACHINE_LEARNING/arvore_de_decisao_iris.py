# -*- coding: utf-8 -*-
"""Arvore de decisao-iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5VbxjQCTUHEKPpIP-pDlOvxdDpe-9kd

# Árvore de decisão


Ilustra o funcionamento do algoritmo de árvore de decisão com atributos numéricos.

Este notebook foi desenvolvido para o ambiente GOOGLE COLAB ([colab.research.google.com](https://colab.research.google.com)).

Prof. Hugo de Paula

-------------------------------------------------------------------------------

### Base de dados: Iris dataset (espécies de lírios)

https://archive.ics.uci.edu/ml/datasets/Iris/

3 classes (setosa, virginica, versicolor)

50 amostras por classe

4 atributos reais positivos (comp. pétala, comp. sépala, larg. pétala, larg. sépala)
"""

!pip install pydotplus
!pip install dtreeviz

import pandas as pd
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

"""### Carga dos dados e particionamento das bases de treinamento e teste

<code>train_test_split(X, y) -- particiona a base de dados original em bases de treinamento e teste.</code>

Por padrão, 75% da base é utilizada para treinamento e 25% para testes. No código a seguir, são utilizados 15% para teste e 85% para treinamento.
"""

# importa a base de dados iris
iris = datasets.load_iris()

X, y = iris.data, iris.target
class_names = iris.target_names

# Particiona a base de dados
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.15)

"""### Indução do Modelo


Os três passos para indução de um modelo são:

1.   Instanciar o modelo: ``` DecisionTreeClassifier()```
2.   Treinar o modelo: ```fit()```
3.   Testar o modelo: ```predict()```
"""

tree_iris = DecisionTreeClassifier(random_state=0, criterion='entropy', class_weight=[{0: 1, 1: 1})
tree_iris = tree_iris.fit(X_train, y_train)
print("Acurácia (base de treinamento):", tree_iris.score(X_train, y_train))

y_pred = tree_iris.predict(X_test)
print("Acurácia de previsão:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))

cnf_matrix = confusion_matrix(y_test, y_pred)
cnf_table = pd.DataFrame(data=cnf_matrix, index=iris.target_names, columns=[x + "(prev)" for x in iris.target_names])
print(cnf_table)

"""### Exibição da árvore de decisão"""

from dtreeviz.trees import *

viz = dtreeviz(tree_iris,
              X_train,
              y_train,
              target_name="espécie",
              feature_names=iris.feature_names,
              class_names=["setosa", "versicolor", "virginica"])  

viz.view()

import pydotplus 
# Create DOT data
dot_data = tree.export_graphviz(tree_iris, out_file=None, 
                                #proportion=True,
                                rounded =True,
                                filled=True,
                                feature_names=iris.feature_names,  
                                class_names=["setosa", "versicolor", "virginica"])

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)  

# Show graph
Image(graph.create_png())