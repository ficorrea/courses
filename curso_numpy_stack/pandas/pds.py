import numpy as np

X = []
for line in open('data_2d.csv'):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)
X = np.array(X)
X.shape

# Import
import pandas as pd
x = pd.read_csv('data_2d.csv', header=None)
x.shape
x.info()
x.head()
x = x.as_matrix()
x[0]
x[x[0] < 5]

df = pd.read_csv('international_passengers.csv',
                 engine='python', skip_footer=3)
df.columns = ['month', 'passengers']
df['passengers']
df.passengers
df['ones'] = 1
df.head()

# Apply
from datetime import datetime
datetime.strptime('1949-05', '%Y-%m')
df['dt'] = df.apply(lambda row: datetime.strptime(
    row['month'], '%Y-%m'), axis=1)
df.info()

# Join
df1 = pd.read_csv('table1.csv')
df2 = pd.read_csv('table2.csv')
m = pd.merge(df1, t2, on='user_id')
df1.merge(df2, on='user_id')
