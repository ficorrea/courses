#Importando as bibliotecas

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando dataset
dataset = pd.read_csv('01 - Preprocessamento/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
