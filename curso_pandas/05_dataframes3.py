# Dataframes 3

import pandas as pd
bond = pd.read_csv('datasets/jamesbond.csv')

# Métodos .set_index() e .reset_index()
bond.set_index('Film', inplace=True)
bond.head(10)

# Recuperar linhas pelo nome do índice com .loc[]
bond.sort_index(inplace=True)
bond.loc['Goldfinger']
bond.loc['Casino Royale']
bond.loc['Diamonds Are Forever' : 'Goldfinger']
bond.loc[['Octopussy', 'Moonraker']]
bond.loc[['Live and Let Die', 'Gold Bond']]

# Recuperar linhas pelo nome do índice com .iloc[]
bond.loc[15]
bond.iloc[15]
bond.iloc[[15, 20, 10]]
bond.iloc[4:8]
bond.iloc[3]

# Método catch-all .ix[]
bond.ix['GoldenEye']
bond.ix['Goldfinger' : 'Diamonds Are Forever']
bond.ix[10:15]
bond.ix[['Spectre', 'Sacred Bond']] # neste caso serão exibidas as 2 linhas, mesmo que uma delas não exista
bond.ix[[8, 30]] # Aqui será gerado um erro

# Segundos argumentos nos métodos .loc[], .iloc[], .ix[]
bond.loc['Moonraker', 'Director' : 'Budget']
bond.loc['Moonraker', ['Director', 'Budget', 'Actor']]
bond.iloc[4, 2:5]
bond.iloc[4, [2, 5, 3]]
bond.ix[20, 'Budget']
bond.ix['Moonraker', 1:4]

# Setando dados em uma específica célula
bond.ix['Dr. No']
bond.ix['Dr. No', 'Actor'] = 'Sir Sean Connery'
bond.ix['Dr. No', ['Box Office', 'Budget']] = [450.7, 10]

# Setando dados em mais de uma célula
mask = bond['Actor'] == 'Sean Connery'
bond[mask]['Actor'] = 'Sir Sean Connery' # com esta operação é necessário criar uma cópia do dataset
bond.ix[mask, 'Actor'] = 'Sir Sean Connery'

# Renomeando colunas ou indíces
bond.rename(columns={'Year' : 'Release', 'Box Office' : 'Revenue'}, inplace=True)
bond.rename(index={'Dr. No' : 'Doctor No'}, inplace=True)
bond.columns = ['Year Release', 'Actor', 'Director', 'Gross', 'Cost', 'Salary']

# Deletando linhas ou colunas
# axis 0 linhas, 1 colunas
bond.drop(['Casino Royale', 'Skyfall'], inplace=True)
bond.drop(labels=['Director', 'Year Release'], axis=1, inplace=True)
actor = bond.pop('Actor')
del bond['Cost']

# Criando exemplos randômicos
bond.sample()
bond.sample(n=5, axis=1)
bond.sample(frac=0.30)

# Métodos .nsmallest() e .nlargest()
bond.nlargest(3, 'Box Office')
bond.nsmallest(3, 'Box Office')

# Filtrando com método .where()
mask = bond['Actor'] == 'Sean Connery'
mask2 = bond['Box Office'] > 800
bond.where(mask & mask2)

# Método .query()
bond.columns = [column_name.replace(' ', '_') for column_name in bond.columns]
bond.query('Actor == "Sean Connery"')
bond.query('Actor == "Roger Moore" and Director == "John Glen"')
bond.query('Actor in ["Timothy Dalton", "Sean Connery"]')
bond.query('Actor not in ["Timothy Dalton", "Sean Connery"]')

# Método .apply() com valores das linhas
def good_movie(row):
    actor = row[1]
    budget = row[4]
    if actor == 'Pierce Brosnan':
        return 'The best'
    elif actor == 'Roger Moore' and budget > 40:
        return 'Enjoyable'
    else:
        return 'I have no clue'

bond.apply(good_movie, axis=1)

# Método .copy()
# este método cria uma cópia exata do objeto escolhido, podendo manipulá-lo 
# da mesma forma que o original
directors = bond['Director'].copy()
directors['A View to a Kill'] = 'Mister John Glen'
directors.head(3)
