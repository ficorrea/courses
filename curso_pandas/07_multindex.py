# Módulo MultiIndex
import pandas as pd
bigmac = pd.read_csv('datasets/bigmac.csv', parse_dates=['Date']) 

# Criando um multindex com .set_index()
bigmac.set_index(['Date','Country'], inplace=True)
bigmac.sort_index(inplace=True)
bigmac.index

# Método .get_level_values()
bigmac = pd.read_csv('datasets/bigmac.csv', parse_dates=['Date'], index_col=['Date', 'Country'])
bigmac.sort_index(inplace=True)
bigmac.index.get_level_values(1)
bigmac.index.get_level_values('Date')

# Método .set_names()
bigmac.index.set_names(['Day', 'Location'], inplace=True)

# Método .sort_ìndex()
bigmac.sort_index(ascending=[True, False], inplace=True)

# Extraindo linhas de um dataframe multindex
bigmac.loc[('2010-01-01', 'Brazil'), 'Price in US Dollars']
bigmac.loc[('2015-07-01', 'Chile'), 'Price in US Dollars']
bigmac.ix[('2015-07-01', 'China'), 0]

# Método .transpose()
bigmac = bigmac.transpose()
bigmac.ix['Price in US Dollars', ('2016-01-01', 'Denmark')]

# Método .swaplevel()
bigmac = bigmac.swaplevel()

# Método .stack()
world = pd.read_csv('datasets/worldstats.csv', index_col=['country', 'year'])
world.stack().to_frame()

# Método .unstack()
s = world.stack()
s.unstack().unstack().unstack()
s.unstack(0)
s.unstack(-1)
s.unstack('year')
s.unstack(level=[1, 0])
s.unstack(level=['country', 'year'])
s.unstack('year', fill_value=0)

# Método .pivot()
sales = pd.read_csv('datasets/salesmen.csv', parse_dates=['Date'])
sales['Salesman'] = sales['Salesman'].astype('category')
sales.pivot(index='Date', columns='Salesman', values='Revenue')

# Método .pivot_table()
food = pd.read_csv('datasets/foods.csv')
food.pivot_table(values='Spend', index='Gender', aggfunc='mean')
food.pivot_table(values='Spend', index='Item', aggfunc='sum')
food.pivot_table(values='Spend', index=['Gender', 'Item'], columns='City', aggfunc='sum')
food.pivot_table(values='Spend', index=['Gender', 'Item'], columns=['Frequency', 'City'], aggfunc='max')
pd.pivot_table(data=food, values='Spend', index=['Gender', 'Item'], columns=['Frequency', 'City'], aggfunc='max')

# Método pd.melt()
quarters = pd.read_csv('datasets/quarters.csv')
pd.melt(quarters, id_vars='Salesman')
pd.melt(quarters, id_vars='Salesman', var_name='Quaters', value_name='Revenue')
