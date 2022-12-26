import pandas as pd
import random

dataset = pd.read_excel('RELATORIO BAIRRO.xls')
bairros = dataset.iloc[:, 0:1]

codigos_random = random.sample(list(range(1, len(bairros) + 1)), len(bairros))

code = []
for c in codigos_random:
    code.append(str(c))

codigos = pd.DataFrame(data=code, columns=['CODIGOS'])

lista_bairros = pd.merge(bairros, codigos, how='left', left_on=['BAIRROS'], 
                         right_on=['CODIGOS'], left_index=True, 
                         right_index=True, copy=True)


with open('bairros.csv', 'w') as _file:
    _file.write('BAIRROS, CODIGOS \n' )
    for i in range(len(lista_bairros)):
        _file.writelines((lista_bairros['BAIRROS'][i] + ', ', lista_bairros['CODIGOS'][i], '\n'))
    _file.close()






