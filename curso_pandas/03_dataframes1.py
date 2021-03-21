# Dataframes 1

import pandas as pd
nba = pd.read_csv('datasets/nba.csv')

# Shared Methods and Attributes
nba.head(1)
nba.tail(1)
nba.index
nba.values
nba.shape
nba.dtypes
nba.columns
nba.axes
nba.info()
nba.get_dtype_counts()

# Diferenças entre métodos compartilhados
rev = pd.read_csv('datasets/revenue.csv', index_col='Date')
rev.head(3)
rev.sum(axis=0)
rev.sum(axis=1) #rev.sum(axis='columns')

# Selecionando uma coluna de um Dataframe
nba.head(3)
nba.Name
nba.Salary
nba['Name']
nba['Salary']
nba['Name'].head()

# Selecionando duas ou mais colunas de um Dataframe
nba[['Name', 'Salary']]
nba[['Number', 'Team', 'College']].head()
select = ['Salary', 'Number', 'Team']
nba[select]

# Adicionando colunas a um Dataframe
nba['Sport'] = 'Basketball'
nba.head(3)
nba.insert(4, column='Teste', value=100)
nba.head(3)

# Broadcasting Operations
nba = pd.read_csv('datasets/nba.csv')
nba['Age'].add(5)
nba['Age'] + 5
nba['Salary'].sub(5000000)
nba['Weight'].mul(0.453592)
nba.insert(7, column='Weight in Kg', value=nba['Weight'].mul(0.453592))
nba.head()
nba['Salary'].div(10000)

# Review .value_counts()
nba = pd.read_csv('datasets/nba.csv')
nba['Team'].value_counts()
nba['Position'].value_counts()
nba['Salary'].value_counts()

# Drop colunas com valores nulos
nba.dropna()
nba.dropna(how='all')
nba.dropna(subset=['Salary', 'College'], inplace=True)
nba.head(3)

# Fill em valores nulos com .fillna()
nba = pd.read_csv('datasets/nba.csv')
nba.fillna(0) # Muda em todas as colunas
nba['Salary'].fillna(0, inplace=True)
nba.head()
nba['College'].fillna('No College', inplace=True)
nba.head(5)

# Método .astype()
nba = pd.read_csv('datasets/nba.csv').dropna(how='all')
nba['Salary'].fillna(0, inplace=True)
nba['College'].fillna('None', inplace=True)
nba.head()
nba['Salary'] = nba['Salary'].astype('int')
nba['Number'] = nba['Number'].astype('int')
nba['Age'] = nba['Age'].astype('int')
nba['Position'].nunique()
nba['Position'] = nba['Position'].astype('category') # Categorizar diminui o tamanho da memória utilizada

# Métodos .sort_values() e .sort_index()
nba = pd.read_csv('datasets/nba.csv')
nba.sort_values('Name', ascending=False)
nba.sort_values('Salary', ascending=False, inplace=True)
nba.sort_values(['Name', 'Team'], ascending=[False, True])
nba.sort_index()

# Método Rank
nba = pd.read_csv('datasets/nba.csv').dropna(how='all')
nba['Salary'].fillna(0, inplace=True).astype('int')
nba['Salary Rank'] = nba['Salary'].rank().astype('int')
nba.head()
