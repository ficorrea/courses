# Aula 23
# Creating a series object from a python list
import pandas as pd
ice_cream = ['chocolate', 'baunilha', 'morango', 'rum']
pd.Series(ice_cream)

loteria = [4, 8, 15, 16, 23, 42]
pd.Series(loteria)

registros = [True, False, True, False, False, True]
pd.Series(registros)

#Aula 24
#Creating a series object from a dictionary
webster = {'Vaca': 'Animal', 'Banana' : 'Fruta', 'Cinza' : 'Cor'}
s = pd.Series(webster)

# Aula 28
# Import series with read_csv method
pokemon = pd.read_csv('datasets/pokemon.csv', usecols=['Pokemon'], squeeze=True)
google = pd.read_csv('datasets/google_stock_price.csv', squeeze=True)

# Aula 29
# head and tail
pokemon.head()
google.tail()

# Aula 30
# Built-in functions
len(pokemon)
len(google)
sorted(google)
dict(pokemon)

# AUla 31
# More series attibutes
google.dtype
pokemon.is_unique
google.is_unique
pokemon.ndim

# Aula 32
# sort_values() method
pokemon.sort_values()
pokemon.sort_values(ascending=False)

# Aula 33
# Inplace parameter
google = google.sort_values()
google.head()
google.sort_index()

# Aula 36
# Extract values seies by index position
pokemon[1]
pokemon[[100, 200, 300]]
pokemon[50:101]
pokemon[:50]
pokemon[-30:]
pokemon[-30: -10]

# Aula 37
# Extract values by index values
pokemon = pd.read_csv('datasets/pokemon.csv', index_col='Pokemon', squeeze=True)
pokemon[0]
pokemon[['Noibat', 'Diancie']]
pokemon[['Diancie', 'Digimon']]

# Aula 38
# The get() method
pokemon.get('Digimon')
pokemon.get('Diancie')

# Aula 39
# Math in Series
google = pd.read_csv('datasets/google_stock_price.csv', squeeze=True)
google.head()
google.count()
google.sum()
google.mean()
google.std()
google.min()
google.median()
google.mode()
google.describe()

# Aula 40
# idmax() and idmin()
# Retorna o indice que esta com a maior ou menor posição
google.idxmax()
google.idxmin()

# Aula 41
# The .values_counts() method
pokemon.value_counts()
pokemon.value_counts(ascending=True)

# Aula 42
# The apply() method
google.head(6)
def performance(number):
    if number < 300:
        return 'OK'
    elif number >= 300 and number < 600:
        return 'Satisfatorio'
    else:
        return 'Incrível!'
google.apply(performance)
google.apply(performance).value_counts()
google.apply(lambda price : price / 100)

# Aula 43
# .map() method
pokemon_names = pd.read_csv('datasets/pokemon.csv', usecols=['Pokemon'], squeeze=True)
pokemon_types = pd.read_csv('datasets/pokemon.csv', index_col='Pokemon', squeeze=True)
pokemon_names.map(pokemon_types)
pokemon_types = pd.read_csv('datasets/pokemon.csv', index_col='Pokemon', squeeze=True).to_dict()
pokemon_names.map(pokemon_types)
