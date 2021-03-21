# Merging, joining and concatening
import pandas as pd

week1 = pd.read_csv('datasets/Restaurant - Week 1 Sales.csv')
week2 = pd.read_csv('datasets/Restaurant - Week 2 Sales.csv')
customers = pd.read_csv('datasets/Restaurant - Customers.csv')
foods = pd.read_csv('datasets/Restaurant - Foods.csv')

# Método .concat()
pd.concat([week1, week2], ignore_index=True)
sales = pd.concat([week1, week2], keys=['A', 'B'])
sales.loc[('B', 240), 'Customer ID']

# Método .append()
week1.append(week2, ignore_index=True)

# Inner Joins
week1.merge(week2, how='inner', on='Customer ID', suffixes=[' - A', ' - B'])
week1.merge(week2, how='inner', on=['Customer ID', 'Food ID'])

# Outer Joins
merged = week1.merge(week2, how='outer', on='Customer ID', suffixes=[' - Week 1', ' - Week 2'], 
            indicator=True)
merged['_merge'].value_counts()
merged['_merge'].isin(['left_only', 'right_only'])

# Left Joins
week1.merge(foods, how='left', on='Food ID', sort=True)

# Parâmetros left_on e right_on
week2.merge(costumers, how='left', left_on='Customer ID', right_on='ID', 
            sort=True).drop('ID', axis=1)

# Merging com left_index e right_index
foods = pd.read_csv('datasets/Restaurant - Foods.csv', index_col='Food ID')
customers = pd.read_csv('datasets/Restaurant - Customers.csv', index_col='ID')
sales = week1.merge(customers, how='left', left_on='Customer ID', right_index=True)
"""left e right index são 
   booleanos, por isso precisa 
   alterar o index_col no dataset"""
sales.merge(foods, how='left', left_on='Food ID', right_index=True)
week1.merge(week2, how='left', left_index=True, right_index=True)

# Método .join()
satisfaction = pd.read_csv('datasets/Restaurant - Week 1 Satisfaction.csv')
week1.join(satisfaction)

# Método pd.merge()
