import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

# Método .plot()
bb = data.DataReader(name='FORD', data_source='iex', start='2013-07-01', end='2017-12-31')
bb.head()
bb.plot(y=['low', 'high'])
bb['close'].plot()

# Modificando estéticas
plt.style.available
plt.style.use('fivethirtyeight')
bb.plot(y='close')
plt.style.use('dark_background')
bb.plot(y='close')
plt.style.use('ggplot')
bb.plot(y='close')

# Barras
def rank(price):
    if price <= 1.2:
        return 'Poor'
    elif price > 1.2 and price <= 1.6:
        return 'Satisfactory'
    else:
        return 'Great'

bb['close'].apply(rank).value_counts().plot(kind='bar')
bb['close'].apply(rank).value_counts().plot(kind='barh')


# Pizza
bb['close'].mean()

def media(valor):
    if valor >= 1.2914326512455514:
        return 'Acima da média'
    else:
        return 'Abaixo da média'

bb['close'].apply(media).value_counts().plot(kind='pie', legend=True)

# Histogramas
def number(valor):
    return int(valor * 10)

plt.style.use('ggplot')
bb['high'].apply(number).value_counts()
bb['high'].apply(number).value_counts().nunique()
bb['high'].apply(number).value_counts().plot(kind='hist', bins=15)





