import pandas as pd

# files = [f'datatran{i}.csv' for i in range(2007, 2022)]
files = [f'acidentes{i}.csv' for i in range(2007, 2022)]

# path = '/home/felipecorrea/Documents/prf_acidentes/ocorrência/'
path = '/home/felipecorrea/Documents/prf_acidentes/pessoa/'

df_final = pd.DataFrame()

for f in files:
    df_temp = pd.read_csv(f'{path}{f}', sep=';')
    df_final = pd.concat([df_final, df_temp])
    # print(df_final.shape)

df_final.to_csv(
    path_or_buf=f'{path}/data_pessoa.csv', 
    sep=',',
    header=True, 
    index=False, 
    decimal='.')