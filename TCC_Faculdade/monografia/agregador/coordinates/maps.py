import googlemaps
import pandas as pd
from unicodedata import normalize

gmaps = googlemaps.Client(key='')

dataset = pd.read_csv('nomes_bairros.csv')
dataset['bairro'] = dataset['bairro'].str.strip()


""" def retirar_acento(texto):
    # Retira o acento das palavras.
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


for i in range(len(dataset['BAIRROS'])):
    dataset['BAIRROS'][i] = retirar_acento(dataset['BAIRROS'][i]) """

bairros = dataset.iloc[:, 0].values
# codigos = dataset.iloc[:, -1].values

latitudes, longitudes = [], []
for bairro in bairros:
    bairro = bairro + ' - MONTES CLAROS - MG'
    g_result = gmaps.geocode(bairro)
    if g_result != []:
        temp = g_result[0]
        temp = temp['geometry'].get('location')
        latitudes.append(temp.get('lat'))
        longitudes.append(temp.get('lng'))
    else:
        latitudes.append('null')
        longitudes.append('null')


def convert_string(lista):
    conv = []
    for l in lista:
        conv.append(str(l))
    return conv

# codigos = convert_string(codigos)


latitudes = convert_string(latitudes)
longitudes = convert_string(longitudes)

with open('bairros_new.csv', 'w') as _file:
    _file.write('BAIRROS,LATITUDE,LONGITUDE\n')
    for bairro, latitude, longitude in zip(bairros, latitudes, longitudes):
        _file.writelines((bairro, ',', latitude, ',', longitude, '\n'))
    _file.close()
