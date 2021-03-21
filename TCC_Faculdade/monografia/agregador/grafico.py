from preprocessing import preprocessamento, missing
import matplotlib.pyplot as plt
import numpy as np

pre = preprocessamento.Preprocessamento()

df1, df2, df3, df4, df5 = map(
    pre.ler_csv, ['imob1.csv', 'imob2.csv', 'imob3.csv',
                  'imob4.csv', 'imob5.csv'])

# ****** Dropar suítes *******

lista = [df1, df2, df3, df4, df5]


df3['banheiros'] = df3['suites']
df4['banheiros'] = df4['suites']

for l in lista:
    l.drop(columns='suites', inplace=True)


bairros = pre.ler_csv('nomes_bairros.csv')
bairros = pre.ajustar_texto(bairros)
bairros = pre.ajustar_nomes_bairros(bairros)

dataset = pre.concatenar_datasets([df1, df2, df3, df4, df5])
dataset = dataset.iloc[:, 2:]
dataset = pre.ajustar_texto(dataset)
dataset = pre.ajustar_nomes_bairros(dataset)
#coordenadas = pre.ler_csv('bairros_e_coordenadas.csv')
#dataset = pre.inserir_coordenadas_geograficas(dataset, coordenadas)
# print(dataset['bairro'].value_counts())

# ************** Gráficos valores nulos ou zero **************


def porcentagem(dataset, coluna, valor):
    total = dataset.loc[dataset[coluna] <= valor, coluna]
    return (len(total) / len(dataset)) * 100


# print(dataset.loc[dataset['quartos'] == 5])

""" perc_quartos = porcentagem(dataset, 'quartos', 0)
perc_banheiros = porcentagem(dataset, 'banheiros', 0)
perc_garagens = porcentagem(dataset, 'garagens', 0)
perc_areas = porcentagem(dataset, 'area', 10)
perc_valores = porcentagem(dataset, 'valor', 0)

comodos = ['Quartos', 'Banheiros', 'Garagens', 'Áreas', 'Valores']
valores = [perc_quartos, perc_banheiros,
           perc_garagens, perc_areas, perc_valores] """

""" from bokeh.plotting import figure, show
p = figure(x_range=comodos, title='Porcentagem de valores nulos',
           plot_height=400, plot_width=500)
p.xaxis.major_label_text_font_size = '11pt'
p.yaxis.axis_label = 'Porcentagem'
p.yaxis.major_label_text_font_size = '11pt'
p.vbar(x=comodos, top=valores, width=0.7, color='green')
show(p) """

""" fig, ax = plt.subplots()
index_x = np.arange(len(valores))
largura = 0.4
ax.bar(index_x, valores, largura)
ax.set_ylabel('Porcentagem')
ax.set_title('Porcentagem de valores nulos')
ax.set_xticks(index_x)
ax.set_xticklabels(comodos)
plt.show() """


# Tratamento dos elementos faltantes para visualização

""" dataset.loc[dataset['area'] >= 300, 'area'] = dataset['area'].mean()
dataset.loc[dataset['valor'] >= 2000000, 'valor'] = dataset['valor'].mean()
dataset.loc[dataset['valor'] < 30000, 'valor'] = dataset['valor'].mean() """


# dataset = missing.imputer_media(dataset, 'valor')
""" dataset = missing.imputer_media_grupo(
    dataset, 'quartos', 'valor', [1, 2, 3, 4, 5])
dataset = missing.imputer_media(dataset, 'quartos')
dataset = missing.imputer_media(dataset, 'banheiros')
# dataset = missing.imputer_media(dataset, 'garagens')
# dataset = missing.imputer_media(dataset, 'suites')
dataset = missing.imputer_knn(dataset, 'area', 4, 5)
# dataset = missing.imputer_media_grupo(dataset, 'quartos', 'area', range(1, 6)) """

# print(dataset)

""" m = dataset['quartos'] == 1
m2 = dataset['area'] >= 100.0
m3 = dataset['area'] < 100.0
dataset.loc[m & m2, 'area'] = dataset.loc[m & m3, 'area'].mean() """

""" dataset.loc[dataset['bairro'] == 'Belvedere'] = np.nan
dataset.dropna(inplace=True) """


def graf(dataset, y, nome_coluna, numero_coluna):
    x = dataset.iloc[:, numero_coluna].values
    plt.scatter(x, y)
    plt.title('{} x Valor'.format(nome_coluna))
    plt.xlabel(nome_coluna)
    plt.ylabel('Valor')
    plt.show()


def bairro(nome):
    mask = dataset['bairro'] == nome
    data = dataset.loc[mask]
    x = data.iloc[:, 0:7]
    y = data.iloc[:, 7].values
    return x, y

# ************** Gráficos gerais **************


""" from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

p1 = figure(plot_height=300, plot_width=400,
            title='Variáveis independentes no hiperplano')
p1.xaxis.axis_label = 'Quartos'
p1.yaxis.axis_label = 'Valores'
p1.circle(x=dataset.iloc[:, 3].values,
          y=dataset.iloc[:, 7].values, color='blue', size=3)

p2 = figure(plot_height=300, plot_width=400)
p2.xaxis.axis_label = 'Banheiros'
# p2.yaxis.axis_label = 'Valores'
p2.circle(x=dataset.iloc[:, 4].values,
          y=dataset.iloc[:, 7].values, color='red', size=3)

p3 = figure(plot_height=300, plot_width=400)
p3.xaxis.axis_label = 'Garagens'
p3.yaxis.axis_label = 'Valores'
p3.circle(x=dataset.iloc[:, 5].values,
          y=dataset.iloc[:, 7].values, color='green', size=3)

p4 = figure(plot_height=300, plot_width=400)
p4.xaxis.axis_label = 'Áreas'
# p4.yaxis.axis_label = 'Valores'
p4.circle(x=dataset.iloc[:, 6].values,
          y=dataset.iloc[:, 7].values, color='navy', size=3)

grid = gridplot([[p1, p2], [p3, p4]])
show(grid) """

""" fig = plt.figure(1)
fig.suptitle('Variáveis independentes no hiperplano')
plt.title('Cômodos no hiperplano')
plt.subplot(3, 2, 1)
plt.ylabel('Valores')
plt.xlabel('Quartos')
plt.scatter(dataset.iloc[:, 3].values, dataset.iloc[:, 7].values, c='blue')
plt.subplot(3, 2, 2)
plt.ylabel('Valores')
plt.xlabel('Banheiros')
plt.scatter(dataset.iloc[:, 4].values, dataset.iloc[:, 7].values, c='red')
plt.subplot(3, 2, 3)
"""""" plt.ylabel('Valores')
plt.xlabel('Suítes')
plt.scatter(dataset.iloc[:, 5].values, dataset.iloc[:, 7].values, c='cyan')
plt.subplot(3, 2, 4) """"""
plt.ylabel('Valores')
plt.xlabel('Garagens')
plt.scatter(dataset.iloc[:, 5].values, dataset.iloc[:, 7].values, c='green')
plt.subplot2grid((3, 3), (2, 0), colspan=3)
plt.scatter(dataset.iloc[:, 6].values, dataset.iloc[:, 7].values, c='magenta')
plt.xlabel('Áreas')
plt.ylabel('Valor')
plt.subplots_adjust(wspace=0.5, top=0.9, hspace=0.5)
plt.figure(2)
plt.title('Variável área no hiperplano')
plt.scatter(dataset.iloc[:, 6].values, dataset.iloc[:, 7].values, c='magenta')
plt.show() """

# valores = dataset.iloc[:, 7].values  # Valores dos apartamentos
# Quartos
# graf(dataset, valores, 'Quartos', 3)
# Banheiros
# graf(dataset, valores, 'Banheiros', 4)
# Áreas
# graf(dataset, valores, 'Área', 6)

# ************* Gráficos por bairro *************

""" nome = 'Ibituruna'
x, y = bairro(nome) """
# Quartos
# graf(x, y, 'Quartos', 3)
# Banheiros
# graf(x, y, 'Banheiros', 4)
# Área
# graf(x, y, 'Áreas', 7)


# ************** Matriz de correlação **************
""" import seaborn as sns
data = dataset.iloc[:, 2:]
corr = data.corr()
sns.heatmap(corr, cmap='hot')
plt.show() """

""" data = dataset.iloc[:, 1:]
corr = data.corr()
plt.imshow(corr, cmap='hot')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.show() """

""" print(dataset['bairro'].value_counts())
print(dataset['quartos'].value_counts())

print(dataset.loc[dataset['quartos'] == 4]) """
# print(dataset.loc[dataset['quartos'] == 5])

# print(dataset)


""" print(dataset.loc[m])

mask = list(range(len(dataset.loc[dataset['quartos'] == 1, 'quartos'])))
mask2 = list(dataset.loc[dataset['quartos'] == 1, 'valor'].values)


plt.scatter(mask, mask2)
plt.show() """

""" import folium
import pandas as pd
montes_claros = (-16.72, -43.88)
data = pd.read_csv('dados.csv')
data = pre.inserir_coordenadas_geograficas(data, coordenadas)
# print(data)
map = folium.Map(location=montes_claros, zoom_start=5)
for lat, long, qtd, cor in zip(data['latitude'], data['longitude'], data['quantidade'], data['cor']):
    folium.CircleMarker(location=[lat, long],
                        radius=qtd, color=cor, fill=True, fill_opacity=0.2).add_to(map)
map.save('mapa.html') """

""" from bokeh.plotting import figure, show
import pandas as pd
data = pd.read_csv('dados.csv')
data.sort_values('quantidade', ascending=True, inplace=True)
p = figure(y_range=data['bairro'].values, plot_height=550, plot_width=550)
p.hbar(y=data['bairro'], height=0.5, right=data['quantidade'], color='navy')
p.xaxis.axis_label = 'Quantidade'
p.yaxis.axis_label = 'Bairros'
show(p) """


from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import pandas as pd

data1 = pd.read_csv('temp/p1.csv')
data1.sort_values('quantidade', ascending=True, inplace=True)
data2 = pd.read_csv('temp/p2.csv')
data2.sort_values('quantidade', ascending=True, inplace=True)
data3 = pd.read_csv('temp/p3.csv')
data3.sort_values('quantidade', ascending=True, inplace=True)
data4 = pd.read_csv('temp/p4.csv')
data4.sort_values('quantidade', ascending=True, inplace=True)
data5 = pd.read_csv('temp/p5.csv')
data5.sort_values('quantidade', ascending=True, inplace=True)

p1 = figure(y_range=data1['bairro'].values, plot_height=425,
            plot_width=350, title='Apartamentos com 1 quarto')
p1.hbar(y=data1['bairro'], height=0.5,
        right=data1['quantidade'], color='teal')
p1.yaxis.axis_label = 'Bairros'
p1.xaxis.axis_label = 'Quantidade'
p2 = figure(y_range=data2['bairro'].values, plot_height=425,
            plot_width=450, title='Apartamentos com 2 quartos')
p2.hbar(y=data2['bairro'], height=0.5,
        right=data2['quantidade'], color='teal')
p2.xaxis.axis_label = 'Quantidade'
p3 = figure(y_range=data3['bairro'].values, plot_height=425,
            plot_width=450, title='Apartamentos com 3 quartos')
p3.hbar(y=data3['bairro'], height=0.5,
        right=data3['quantidade'], color='teal')
p3.yaxis.axis_label = 'Bairros'
p3.xaxis.axis_label = 'Quantidade'
p4 = figure(y_range=data4['bairro'].values, plot_height=425,
            plot_width=450, title='Apartamentos com 4 quartos')
p4.hbar(y=data4['bairro'], height=0.5,
        right=data4['quantidade'], color='teal')
p4.xaxis.axis_label = 'Quantidade'
p5 = figure(y_range=data5['bairro'].values, plot_height=400,
            plot_width=450, title='Apartamentos com 5 quartos')
p5.hbar(y=data5['bairro'], height=0.5,
        right=data5['quantidade'], color='teal')
p5.yaxis.axis_label = 'Bairros'
p5.xaxis.axis_label = 'Quantidade'
# grid = gridplot([[p1, p2], [p3, p4], [p5]])
grid = gridplot([[p3, p4]])
show(p5)

""" banheiros, vagas = [], []
for i in range(7):
    banheiros.append(len(dataset.loc[dataset['banheiros'] == i, 'banheiros']))
    vagas.append(len(dataset.loc[dataset['garagens'] == i, 'garagens']))


def percent(data):
    perc = []
    for d in data:
        perc.append(d/670*100)
    return perc


ban = percent(banheiros[0:6])
vag = percent(vagas)

# print(ban, vag)
x = [0, 1, 2, 3, 4, 5, 6]

from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
p1 = figure(plot_height=300, plot_width=300)
p1.yaxis.axis_label = 'Porcentagem'
p1.xaxis.axis_label = 'Quantidade de banheiros'
p1.vbar(x=x[0:6], top=ban, width=0.7, color='mediumseagreen')
p2 = figure(plot_height=300, plot_width=300)
p2.xaxis.axis_label = 'Quantidade de vagas'
p2.vbar(x=x, top=vag, width=0.7, color='crimson')
grid = gridplot([[p1, p2]])
show(grid) """

# print(dataset.loc[dataset['quartos'] == 2, 'bairro'].value_counts())
