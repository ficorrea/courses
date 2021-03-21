# Hierarquical Clustering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values

# Usando dendogramas
import scipy.cluster.hierarchy as sch
dend = sch.dendrogram(sch.linkage(x, method='ward'))
plt.title('Dendograma')
plt.xlabel('Consumidores')
plt.ylabel('Distâncias')
plt.show()

# Fitting Hierarquical Clustering
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(x)

plt.scatter(x[y_hc==0, 0], x[y_hc==0, 1], s=100, c='red', label='Cl1')
plt.scatter(x[y_hc==1, 0], x[y_hc==1, 1], s=100, c='blue', label='Cl2')
plt.scatter(x[y_hc==2, 0], x[y_hc==2, 1], s=100, c='green', label='Cl3')
plt.scatter(x[y_hc==3, 0], x[y_hc==3, 1], s=100, c='cyan', label='Cl4')
plt.scatter(x[y_hc==4, 0], x[y_hc==4, 1], s=100, c='magenta', label='Cl5')
plt.title('Clusters')
plt.xlabel('Annual Income')
plt.ylabel('Spend')
plt.legend()
