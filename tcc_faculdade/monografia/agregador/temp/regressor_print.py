
# coding: utf-8
import pandas as pd
from preprocessing import preprocessamento
pre = preprocessamento.Preprocessamento()

df1, df2, df3, df4, df5 = map(
    pre.ler_csv, ['imob1.csv', 'imob2.csv', 'imob3.csv', 'imob4.csv', 'imob5.csv'])

lista = [df1, df2, df3, df4, df5]

df3['banheiros'] = df3['suites']
df4['banheiros'] = df4['suites']

for l in lista:
    l.drop(columns='suites', inplace=True)

dataset = pre.concatenar_datasets(lista)

mask = dataset['banheiros'] != 0


# In[9]:


dataset.loc[mask, 'banheiros'].mean()


# In[10]:


mask2 = dataset['banheiros'] == 0
dataset.loc[mask2, 'banheiros'] = int(dataset.loc[mask, 'banheiros'].mean())


# In[11]:


dataset.loc[dataset['quartos'] == 0, 'quartos'].count()


# In[12]:


dataset.loc[dataset['quartos'] == 0, 'quartos'] = int(
    dataset.loc[dataset['quartos'] != 0, 'quartos'].mean())


# In[13]:


dataset.loc[dataset['valor'] == 0, 'valor'].count()


# In[14]:


dataset.loc[dataset['valor'] == 0,
            'valor'] = dataset.loc[dataset['valor'] != 0, 'valor'].mean()


# In[15]:


dataset.loc[dataset['area'] == 0,
            'area'] = dataset.loc[dataset['area'] != 0, 'area'].mean()


# In[16]:


dataset = dataset.iloc[:, 2:]


# In[17]:


dataset = pre.ajustar_texto(dataset)
dataset = pre.ajustar_nomes_bairros(dataset)


# In[18]:


x = dataset.iloc[:, 0:5].values
y = dataset.iloc[:, 5].values


# In[19]:


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label = LabelEncoder()
x[:, 0] = label.fit_transform(x[:, 0])


# In[20]:


onehot = OneHotEncoder(categorical_features=[0])
x = onehot.fit_transform(x).toarray()


# In[21]:


x1 = pd.DataFrame(x)


# In[22]:


# Avoiding dummy variable trap
x = x[:, 1:]


# In[23]:


import statsmodels.formula.api as sm
import numpy as np


# In[24]:


x = np.append(arr=np.ones((1358, 1)).astype('int'), values=x, axis=1)


# In[25]:


l = list(range(0, 50))


# In[26]:


x_opt = x[:, l]


# In[27]:


ols = sm.OLS(endog=y, exog=x_opt).fit()
print(ols.summary())

print(ols.summary())
