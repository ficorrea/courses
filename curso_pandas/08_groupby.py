# Groupby

import pandas as pd

fortune = pd.read_csv('datasets/fortune1000.csv', index_col='Rank')
sectors = fortune.groupby('Sector')

# Primeiras operações, método .groupby()
sectors.size() # ordem alfabética
fortune['Sector'].value_counts() # ordem de quantidade
sectors.first()
sectors.last()
sectors.groups # Dict com os grupos
fortune.loc[24] # é loc por se tratar do rank, não do index

# Método .get_group()
sectors.get_group('Energy')
sectors.get_group('Technology')

# Métodos no Groupby Object e DataFrame Columns
sectors.max()
sectors.min()
sectors.sum()
sectors.mean()
sectors['Revenue'].sum()
sectors[['Revenue', 'Profits']].mean()

# Agrupamento por múltiplas colunas
fortune = pd.read_csv('datasets/fortune1000.csv', index_col='Rank')
sectors = fortune.groupby(['Sector', 'Industry'])
sectors.size()
sectors.sum()
sectors['Revenue'].sum()
sectors[['Employees', 'Profits']].mean()

# Método .agg()
fortune = pd.read_csv('datasets/fortune1000.csv', index_col='Rank')
sectors = fortune.groupby('Sector')
sectors.agg({'Revenue' : 'sum', 'Employees' : 'mean', 'Profits' : 'median'})
sectors.agg(['size', 'sum', 'mean'])
sectors.agg({'Revenue' : ['sum', 'median'], 'Employees' : 'mean', 'Profits' : 'median'})

# Interação entre grupos
df = pd.DataFrame(columns=fortune.columns)
for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(2, 'Revenue')
    df = df.append(highest_revenue_company_in_group)

cities = fortune.groupby('Location')
df = pd.DataFrame(columns=fortune.columns)
for city, data in cities:
    highest_revenue_in_city = data.nlargest(1, 'Revenue')
    df = df.append(highest_revenue_in_city)

