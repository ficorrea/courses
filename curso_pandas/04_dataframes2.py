# DataFrames 2

import pandas as pd
df = pd.read_csv('datasets/employees.csv')
df.info()
# Uma das possibilidades de uso:
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['Last Login Time'] = pd.to_datetime(df['Last Login Time'])
df['Senior Management'] = df['Senior Management'].astype('bool')
df['Gender'] = df['Gender'].astype('category')
# ou -> pd.read_csv('dataset', parse_dates=['col1', 'col2'])
# já define e altera o tipo de dados da coluna referente a datas

# Filtrando um df baseado em condição
df = pd.read_csv('datasets/employees.csv', parse_dates=['Start Date', 'Last Login Time'])
df['Senior Management'] = df['Senior Management'].astype('bool')
df['Gender'] = df['Gender'].astype('category')
df.head(3)
df['Gender'] == 'Male'
df[df['Gender'] == 'Male'] # serve com todos os comparativos
mask = df['Team'] == 'Finance'
df[mask]
df[df['Senior Management']]
mask = df['Start Date'] <= '1985-01-01'
df[mask]

# Filtrando com mais de uma condição (AND)
mask1 = df['Gender'] == 'Male'
mask2 = df['Team'] == 'Sales'
df[mask1 & mask2]

# Filtrando com OR
mask1 = df['Senior Management']
mask2 = df['Start Date'] < '1990-01-01'
df[mask1 | mask2]
mask = df['First Name'] == 'Robert'
mask1 = df['Team'] == 'Client Services'
mask2 = df['Start Date'] > '2016-06-01'
df[(mask & mask1) | mask2] # Combinando AND e OR

# The .isin() método
mask = df['Team'].isin(['Legal', 'Sales', 'Marketing'])
df[mask]

# Métodos .isnull() e .notnull()
mask = df['Team'].isnull()
df[mask]
mask = df['Gender'].notnull()
df[mask]

# Método .between()
mask = df['Salary'].between(60000, 70000)
df[mask]
df[df['Start Date'].between('1991-01-01', '1992-12-31')]
df[df['Last Login Time'].between('08:30am', '12:00pm')]

# Método .duplicated()
# verifica valores duplicados, sem parâmetro o primeiro valor original
# é caracterizado como False
df.sort_values('First Name', inplace=True)
df['First Name'].duplicated(keep=False)
# ~ inverte a lógica, portanto serão mostrados somente valores únicos
mask = ~df['First Name'].duplicated(keep=False)
df[mask]

# Método .drop.duplicates()
len(df)
df.drop_duplicates(subset=['First Name'], keep='first')
df.drop_duplicates(subset=['Team', 'First Name'])

# Método .unique(), .nunique()
df['Gender'].unique()
df['Team'].nunique()
df['Team'].nunique(dropna=False)
