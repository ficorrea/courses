# Processamento de Linguagem Natural

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

# Preprocessamento do texto
import re
import nltk
nltk.download('stopwords') # download do dataset que contém expressões não relevantes
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] # set para algoritmo rodar mais rápido
    review = ' '.join(review)
    corpus.append(review)

# Bag Words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500) # max_features limita a quantidade de palavras
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Treinamento com Naive Bayes
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)









