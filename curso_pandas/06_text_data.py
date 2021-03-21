# Working with text data

import pandas as pd
chicago = pd.read_csv('datasets/chicago.csv').dropna(how = 'all')
chicago['Department'] = chicago['Department'].astype('category')
chicago.info()
chicago['Department'].nunique()
chicago['Department'].count()

# Métodos comuns .lower(), .upper(), .title(), .len()
'hello world'.title()
chicago['Name'].str.title()
chicago['Position Title'] = chicago['Position Title'].str.title()
chicago['Department'].str.len()

# Método .str.replace()
chicago['Department'] = chicago['Department'].str.replace('MGMNT', 'MANAGEMENT')
chicago['Employee Annual Salary'] = chicago['Employee Annual Salary'].str.replace('$', '').astype('float')

# Métodos de filtragem
mask = chicago['Position Title'].str.lower().str.contains('water')
chicago[mask]
mask = chicago['Position Title'].str.lower().str.startswith('water')
chicago[mask]
mask = chicago['Position Title'].str.lower().str.endswith('ist')
chicago[mask]

# Métodos .strip(), .lstrip(), .rstrip()
chicago['Name'].str.lstrip()
chicago['Name'] = chicago['Name'].str.rstrip().str.lstrip()
chicago['Position Title'] = chicago['Position Title'].str.strip()

# Métodos de string para indíce e colunas
chicago = pd.read_csv('datasets/chicago.csv', index_col='Name').dropna(how = 'all')
chicago.index = chicago.index.str.strip().str.title()
chicago.head()
chicago.columns = chicago.columns.str.upper()

# Método .str.split()
chicago['Name'].str.split(',').str.get(0).str.title().value_counts()
chicago['Position Title'].str.split(' ').str.get(0).value_counts()

# Expansão e n parâmetros de .str.split()
chicago[['Fisrt Name', 'Last Name']] = chicago['Name'].str.split(',', expand=True)
chicago['Position Title'].str.split(' ', expand=True)
chicago['Position Title'].str.split(' ', expand=True, n=1)
chicago.head()
