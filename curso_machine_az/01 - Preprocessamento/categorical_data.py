# Categorical data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('01 - Preprocessamento/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])

# Encoding categorical
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()

# To dummy variables
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)
