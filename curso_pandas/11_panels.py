import pandas as pd
from pandas_datareader import data

companies = ['MSFT', 'GOOG', 'AAPL', 'YHOO', 'AMZN']
p = data.DataReader(name=companies, data_source='google', start='2010-01-01', end='2016-31-12')

p.items
p.major_axis
p.minor_axis
p.axes
p.ndim
p.dtypes
p.shape
p.size
p.values

#Acessando Dataframe com colchetes
p['Volume']
p.Volume
p['Open'].head()

# Acessando com .iloc e .loc
p.loc['Close']
p.loc['Close', '2014-04-08']
p.loc['Close', '2014-04-08', 'GOOG']
p.iloc[3, 200, 3]

# Convertendo Panel em Multindex DF
df = p.to_frame()
df.head()
df.to_panel()

# Método .major_xs()
p.major_axis
p.majos_xs('2016-06-06')

# Método .minor_xs()
p.minor_axis
p.minor_xs('MSFT')

# Método .tranpose()
p.transpose(2, 1, 0)

# Método .swapaxes()
p.swapaxes('items', 'minor')

