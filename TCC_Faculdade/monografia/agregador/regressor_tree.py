import pandas as pd
from preprocessing import preprocessamento, missing
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

pre = preprocessamento.Preprocessamento()

df1, df2, df3, df4, df5 = map(pre.ler_csv, ['imob1.csv', 'imob2.csv',
                                            'imob3.csv', 'imob4.csv',
                                            'imob5.csv'])

lista = [df1, df2, df3, df4, df5]

df3['banheiros'] = df3['suites']
df4['banheiros'] = df4['suites']

for l in lista:
    l.drop(columns='suites', inplace=True)

dataset = pre.concatenar_datasets([df1, df2, df3, df4, df5])
dataset = dataset.iloc[:, 2:]
dataset = pre.ajustar_texto(dataset)
dataset = pre.ajustar_nomes_bairros(dataset)
dataset['valor'] = dataset['valor'].astype(float)

# print(len(dataset))

# Outliers
""" dataset.loc[dataset['area'] >= 600, 'area'] = dataset['area'].mean()
dataset.loc[dataset['valor'] >= 2000000, 'valor'] = dataset['valor'].mean()
dataset.loc[dataset['valor'] < 30000, 'valor'] = dataset['valor'].mean() """

dataset.loc[dataset['area'] >= 300, 'area'] = 0
dataset.loc[dataset['valor'] >= 2000000, 'valor'] = 0
dataset.loc[dataset['valor'] < 30000, 'valor'] = 0


# dataset = missing.imputer_media(dataset, 'valor')
dataset = missing.imputer_media_grupo(
    dataset, 'quartos', 'valor', [1, 2, 3, 4, 5])
dataset = missing.imputer_media(dataset, 'quartos')
dataset = missing.imputer_media(dataset, 'banheiros')
dataset = missing.imputer_knn(dataset, 'area', 4, 5)

m = dataset['quartos'] == 1
m2 = dataset['area'] >= 100.0
m3 = dataset['area'] < 100.0
dataset.loc[m & m2, 'area'] = dataset.loc[m & m3, 'area'].mean()

""" print(dataset.loc[dataset['quartos'] == 1, 'area'].mean())
print(dataset.loc[dataset['quartos'] == 2, 'area'].mean())
print(dataset.loc[dataset['quartos'] == 3, 'area'].mean())
print(dataset.loc[dataset['quartos'] == 4, 'area'].mean())
print(dataset.loc[dataset['quartos'] == 5, 'area'].mean()) """

# print(dataset)

""" dataset.loc[dataset['bairro'] == 'Belvedere'] = np.nan
dataset.dropna(inplace=True) """


def medias(dataset):
    medias_geral = []
    # print('Banheiros,', 'Garagens,', 'Área')
    for i in range(1, 6):
        md_banheiro = dataset.loc[dataset['quartos'] == i, 'banheiros'].mean()
        md_garagem = dataset.loc[dataset['quartos'] == i, 'garagens'].mean()
        md_area = dataset.loc[dataset['quartos'] == i, 'area'].mean()
        medias_geral.append([i, md_banheiro, md_garagem, md_area])
        # print(md_banheiro, ',', md_garagem, ',', md_area)
    return medias_geral


a = medias(dataset)
# print(a)
# print(dataset['bairro'].nunique())


x = dataset.iloc[:, 0:5].values
y = dataset.iloc[:, 5].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label = LabelEncoder()
x[:, 0] = label.fit_transform(x[:, 0])
onehot = OneHotEncoder(categorical_features=[0])
x = onehot.fit_transform(x).toarray()
# Dummy
x = x[:, 1:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(max_depth=20, random_state=0)
regressor.fit(x_train, y_train)
# y_predict = regressor.predict(x_test)

from sklearn.model_selection import cross_val_score
""" acuracia = cross_val_score(regressor, x_train, y_train, cv=10, n_jobs=-1)
print(acuracia.mean())
print(acuracia.std()) """

from sklearn import metrics
""" print(metrics.mean_absolute_error(y_test, y_predict))
print(metrics.r2_score(y_test, y_predict))
print(metrics.explained_variance_score(y_test, y_predict)) """


def diferenca(lista):
    diferenca = []
    for i in range(len(lista) - 1):
        diferenca.append(lista[i+1] - lista[i])
    return diferenca


def tree():
    """ print('Profundidade,', 'Média Validação Cruzada,', 'Desvio-Padrão Validação Cruzada,',
          'Média Erro Absoluto,', 'R²,', 'Variância Explicada') """
    acc = []
    for p in range(1, 101):
        regressor = DecisionTreeRegressor(max_depth=p, random_state=0)
        regressor.fit(x_train, y_train)
        y_predict = regressor.predict(x_test)
        acuracia = cross_val_score(
            regressor, x_train, y_train, cv=10, n_jobs=-1)
        """ print(p, ',', acuracia.mean(), ',', acuracia.std(), ',', metrics.mean_absolute_error(y_test, y_predict),
              ',', metrics.r2_score(y_test, y_predict), ',', metrics.explained_variance_score(y_test, y_predict)) """
        acc.append(acuracia.mean())
    return acc


""" from bokeh.plotting import figure, show
x = tree()
y = diferenca(x)
xx = list(range(1, len(x)))
p = figure(plot_height=300, plot_width=400)
p.line(xx, y)
p.xaxis.axis_label = 'Árvores'
p.yaxis.axis_label = 'Diferença'
show(p) """

# tree()


def random_forest():
    from sklearn.ensemble import RandomForestRegressor
    print('Árvores/Profundidade,', 'Média Validação Cruzada,', 'Desvio-Padrão Validação Cruzada,',
          'Média Erro Absoluto,', 'R²,', 'Variância Explicada')
    for e in range(5, 100, 5):
        for p in range(5, 100, 5):
            regressor = RandomForestRegressor(
                n_estimators=e, max_depth=p, random_state=0)
            regressor.fit(x_train, y_train)
            y_predict = regressor.predict(x_test)
            acuracia = cross_val_score(
                regressor, x_train, y_train, cv=10, n_jobs=-1)
            print(e, '/', p, ',', acuracia.mean(), ',', acuracia.std(), ',', metrics.mean_absolute_error(y_test, y_predict),
                  ',', metrics.r2_score(y_test, y_predict), ',', metrics.explained_variance_score(y_test, y_predict))


# random_forest()


def random_forest_tree():
    p = 20
    print('Árvores/Profundidade,', 'Média Cross,', 'Desvio-Padrão Cross,',
          'Média Erro Absoluto,', 'R^2,', 'Variância Explicada')
    for e in range(5, 105, 5):
        regressor = RandomForestRegressor(
            n_estimators=e, max_depth=20, random_state=0)
        regressor.fit(x_train, y_train)
        y_predict = regressor.predict(x_test)
        acuracia = cross_val_score(
            regressor, x_train, y_train, cv=10, n_jobs=-1)
        print(e, '/', p, ',', acuracia.mean(), ',', acuracia.std(), ',', metrics.mean_absolute_error(y_test, y_predict),
              ',', metrics.r2_score(y_test, y_predict), ',', metrics.explained_variance_score(y_test, y_predict))


# random_forest_tree()

# Gráfico de barra valores reais x preditos
""" ind = np.arange(len(y_test))
larg = 0.3
fig, ax = plt.subplots()
real = ax.bar(ind - larg/2, y_test, larg, color='blue', label='Real')
pred = ax.bar(ind + larg/2, y_predict, larg, color='red', label='Predito')
ax.set_ylabel('Valores')
ax.set_title('Reais x Preditos')
ax.set_xticks(ind)
plt.show() """

""" from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(
    n_estimators=25, max_depth=15, random_state=0)
regressor.fit(x_train, y_train)
# y_predict = regressor.predict(x_test)


def erro_global(real, predito):
    erro = []
    for r, p in zip(real, predito):
        erro.append((r - p)//1000)
    return erro """


# Gráfico histograma erro global
""" from bokeh.plotting import figure, show
erro = erro_global(y_test, y_predict)
p = figure(title='Erro Global', plot_height=400, plot_width=400)
hist, edges = np.histogram(erro, bins=9)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], color='green')
p.xaxis.axis_label = 'Diferença (x10³)'
p.yaxis.axis_label = 'Quantidade'
show(p) """


""" erro = erro_global(y_test, y_predict)
plt.figure()
plt.title('Erro global')
plt.xlabel('Erro')
plt.ylabel('Quantidade')
val = plt.hist(erro, bins=9, color='green', normed=True)
plt.show() """

""" for v in val:
    print(v)

for v in val[2]:
    print(v) """

# erro.sort()
# print(erro)

""" k = 1 + 3.3*np.log10(len(erro))
# print(k)

err = pd.DataFrame(erro)

lista = list(range(len(erro))) """
"""n = 9
divisao = [lista[i:n] for i in range(n)]
print(divisao) """
# print(metrics.mean_squared_error(y_test, y_predict))

""" n = 9
splited = []
len_l = len(lista)
for i in range(n):
    start = int(i*len_l/n)
    end = int((i+1)*len_l/n)
    splited.append(lista[start:end])

for s in splited:
    a = err.iloc[s].values
    print('Grupo: Valor mínimo: ', min(a),
          '\tValor máximo: ',  max(a)) """

""" data = pd.read_csv('res_for_tree.csv')


def improve(dataset):
    i, x = 0, 1
    imp = []
    for p in range(len(dataset) - 1):
        imp.append(dataset[x] - dataset[i])
        i += 1
        x += 1
    return imp


y = data.iloc[:, 1].values
imp = improve(y)
x = range(len(y) - 1)
plt.plot(x, imp)
plt.show() """


# ****** Previsão valor imóvel ******

from sklearn.ensemble import RandomForestRegressor
""" regressor = RandomForestRegressor(
    n_estimators=25, max_depth=15, random_state=0)
regressor.fit(x_train, y_train) """
# y_predict = regressor.predict(x_test)

from sklearn import tree
with open('tree.dot', 'w') as file:
    file = tree.export_graphviz(regressor.fit(x_train, y_train), out_file=file)

""" enc = pd.DataFrame(x[:, 0:44])
bair = pd.DataFrame(dataset['bairro'])
bairros_encoder = pd.merge(
    right=enc, left=bair, right_index=True, left_index=True, how='outer')

bairros_encoder.drop_duplicates(subset=['bairro'], keep='first', inplace=True)
bairros_encoder.sort_values('bairro', inplace=True) """


def lista_encoder(nome_bairro):
    bairro = bairros_encoder.loc[bairros_encoder['bairro'] == nome_bairro]
    return bairro.iloc[:, 1:].values


def previsao_preco(bairro, quartos, banheiros, garagens, area):
    bairro_encoder = lista_encoder(bairro)
    features = np.concatenate(
        (bairro_encoder[0], [quartos, banheiros, area]), axis=0)
    valor_predito = regressor.predict([features])
    """ print('Imóvel no bairro {} com {} quarto(s), {} banheiro(s), {} vaga(s) de garagem e área de {}m². Valor previsto R$ {}'.format(
        bairro, quartos, banheiros, garagens, area, round(valor_predito[0], 2))) """
    return valor_predito


""" previsao_preco('Cidade Nova', 3, 2, 1, 1, 70.0) """

""" previsao_preco('Centro', 1, 1, 0, 40.0)
previsao_preco('Centro', 2, 1, 1, 60.0)
previsao_preco('Centro', 3, 2, 1, 80.0)
previsao_preco('Centro', 4, 3, 1, 100.0)
previsao_preco('Centro', 5, 4, 2, 120.0)
print('\n')
previsao_preco('Ibituruna', 1, 1, 0, 40.0)
previsao_preco('Ibituruna', 2, 1, 0, 60.0)
previsao_preco('Ibituruna', 3, 2, 1, 80.0)
previsao_preco('Ibituruna', 4, 3, 1, 100.0)
previsao_preco('Ibituruna', 5, 4, 2, 120.0)
print('\n')
previsao_preco('Maracana', 1, 1, 0, 40.0)
previsao_preco('Maracana', 2, 1, 0, 60.0)
previsao_preco('Maracana', 3, 2, 1, 80.0)
previsao_preco('Maracana', 4, 3, 2, 100.0)
previsao_preco('Maracana', 5, 4, 2, 120.0)
print('\n')
previsao_preco('Vila Brasilia', 5, 4, 2, 150.0) """

# print(dataset['bairro'].value_counts())

""" bairros = dataset.drop_duplicates(subset=['bairro'], keep='first')
bairros = list(bairros['bairro'].values)
bairros.sort(reverse=True)

apto1 = [1, 1, 1, 70.43]
apto2 = [2, 1, 1, 73.40]
apto3 = [3, 2, 2, 104.85]
apto4 = [4, 2, 2, 150.68]
apto5 = [5, 3, 2, 128.37]

features = [apto1, apto2, apto3, apto4, apto5]


def estimativa_preco(bairros, features):
    valores = []
    precos = []
    for bairro in bairros:
        for feature in features:
            precos.append(previsao_preco(
                bairro, feature[0], feature[1], feature[2], feature[3])//1000)
        precos.append(previsao_preco(
            bairro, features[0], features[1], features[2], features[3])//1000)
        valores.append(precos)
        precos = []
    return valores


precos1 = estimativa_preco(bairros, apto1)
precos2 = estimativa_preco(bairros, apto2)

from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
p1 = figure(y_range=bairros, title='Apartamento de {} quarto(s), {} banheiro(s), {} vagas e área de {}m²'
            .format(apto1[0], apto1[1], apto1[2], apto1[3]), plot_width=500)
p1.xaxis.axis_label = 'Valor (x10³)'
p1.yaxis.axis_label = 'Bairros'
p1.hbar(y=bairros, height=0.5, right=precos1,
        left=0, color='red')
p2 = figure(y_range=bairros, title='Apartamento de {} quarto(s), {} banheiro(s), {} vagas e área de {}m²'
            .format(apto2[0], apto2[1], apto2[2], apto2[3]), plot_width=500)
p2.xaxis.axis_label = 'Valor (x10³)'
p2.yaxis.axis_label = 'Bairros'
p2.hbar(y=bairros, height=0.5, right=precos2, left=0, color='red')
grid = gridplot([[p1, p2]])
show(grid) """
# show(p)

""" bairros.sort()

br1 = bairros[0:5]
br2 = bairros[5:10]
br3 = bairros[10:15]
br4 = bairros[15:20]
br5 = bairros[20:25]
br6 = bairros[25:30]
br7 = bairros[30:35]
br8 = bairros[35:40]
br9 = bairros[40:44]


def variacao_preco(preco):
    variacao = []
    precos = []
    variacao.append(np.array([0]))
    for i in range(len(preco) - 1):
        variacao.append(preco[i+1] - preco[i])
    for v in variacao:
        precos.append(v[0])
    return precos


estima1 = estimativa_preco(br1, features)
estima2 = estimativa_preco(br2, features)
estima3 = estimativa_preco(br3, features)
estima4 = estimativa_preco(br4, features)
estima5 = estimativa_preco(br5, features)
estima6 = estimativa_preco(br6, features)
estima7 = estimativa_preco(br7, features)
estima8 = estimativa_preco(br8, features)
estima9 = estimativa_preco(br9, features)


def retorna_lista_variacao(estimativas):
    precos_variacao = []
    for e in estimativas:
        precos_variacao.append(variacao_preco(e))
    return precos_variacao


pr1 = retorna_lista_variacao(estima1)
pr2 = retorna_lista_variacao(estima2)
pr3 = retorna_lista_variacao(estima3)
pr4 = retorna_lista_variacao(estima4)
pr5 = retorna_lista_variacao(estima5)
pr6 = retorna_lista_variacao(estima6)
pr7 = retorna_lista_variacao(estima7)
pr8 = retorna_lista_variacao(estima8)
pr9 = retorna_lista_variacao(estima9)

x_axis = [1, 2, 3, 4, 5] """


""" from bokeh.plotting import figure, show, save
from bokeh.io import export_png
from bokeh.layouts import gridplot

p1 = figure(plot_width=500, plot_height=300)
p1.line(x_axis, pr1[0], color='blue', legend=br1[0], line_width=2.5)
p1.line(x_axis, pr1[1], color='red', legend=br1[1], line_width=2.5)
p1.line(x_axis, pr1[2], color='green', legend=br1[2], line_width=2.5)
p1.line(x_axis, pr1[3], color='gold', legend=br1[3], line_width=2.5)
p1.line(x_axis, pr1[4], color='aqua', legend=br1[4], line_width=2.5)
p1.yaxis.axis_label = 'Variação (x10³)'
p1.legend.label_text_font_size = '8pt'
p1.legend.location = 'top_left'

p2 = figure(plot_width=500, plot_height=300)
p2.line(x_axis, pr2[0], color='blue', legend=br2[0], line_width=2.5)
p2.line(x_axis, pr2[1], color='red', legend=br2[1], line_width=2.5)
p2.line(x_axis, pr2[2], color='green', legend=br2[2], line_width=2.5)
p2.line(x_axis, pr2[3], color='gold', legend=br2[3], line_width=2.5)
p2.line(x_axis, pr2[4], color='aqua', legend=br2[4], line_width=2.5)
p2.legend.label_text_font_size = '8pt'
p2.legend.location = 'top_left'

p3 = figure(plot_width=500, plot_height=300)
p3.line(x_axis, pr3[0], color='blue', legend=br3[0], line_width=2.5)
p3.line(x_axis, pr3[1], color='red', legend=br3[1], line_width=2.5)
p3.line(x_axis, pr3[2], color='green', legend=br3[2], line_width=2.5)
p3.line(x_axis, pr3[3], color='gold', legend=br3[3], line_width=2.5)
p3.line(x_axis, pr3[4], color='aqua', legend=br3[4], line_width=2.5)
p3.legend.label_text_font_size = '8pt'
p3.legend.location = 'top_left'

p4 = figure(plot_width=500, plot_height=300)
p4.line(x_axis, pr4[0], color='blue', legend=br4[0], line_width=2.5)
p4.line(x_axis, pr4[1], color='red', legend=br4[1], line_width=2.5)
p4.line(x_axis, pr4[2], color='green', legend=br4[2], line_width=2.5)
p4.line(x_axis, pr4[3], color='gold', legend=br4[3], line_width=2.5)
p4.line(x_axis, pr4[4], color='aqua', legend=br4[4], line_width=2.5)
p4.yaxis.axis_label = 'Variação (x10³)'
p4.legend.label_text_font_size = '8pt'
p4.legend.location = 'top_left'

p5 = figure(plot_width=500, plot_height=300)
p5.line(x_axis, pr5[0], color='blue', legend=br5[0], line_width=2.5)
p5.line(x_axis, pr5[1], color='red', legend=br5[1], line_width=2.5)
p5.line(x_axis, pr5[2], color='green', legend=br5[2], line_width=2.5)
p5.line(x_axis, pr5[3], color='gold', legend=br5[3], line_width=2.5)
p5.line(x_axis, pr5[4], color='aqua', legend=br5[4], line_width=2.5)
p5.legend.label_text_font_size = '8pt'
p5.legend.location = 'top_left'

p6 = figure(plot_width=500, plot_height=300)
p6.line(x_axis, pr6[0], color='blue', legend=br6[0], line_width=2.5)
p6.line(x_axis, pr6[1], color='red', legend=br6[1], line_width=2.5)
p6.line(x_axis, pr6[2], color='green', legend=br6[2], line_width=2.5)
p6.line(x_axis, pr6[3], color='gold', legend=br6[3], line_width=2.5)
p6.line(x_axis, pr6[4], color='aqua', legend=br6[4], line_width=2.5)
p6.legend.label_text_font_size = '8pt'
p6.legend.location = 'top_left'

p7 = figure(plot_width=500, plot_height=300)
p7.line(x_axis, pr7[0], color='blue', legend=br7[0], line_width=2.5)
p7.line(x_axis, pr7[1], color='red', legend=br7[1], line_width=2.5)
p7.line(x_axis, pr7[2], color='green', legend=br7[2], line_width=2.5)
p7.line(x_axis, pr7[3], color='gold',
        legend='Prol. Todos Os Santos', line_width=2.5)
p7.line(x_axis, pr7[4], color='aqua', legend=br7[4], line_width=2.5)
p7.xaxis.axis_label = 'Quartos'
p7.yaxis.axis_label = 'Variação (x10³)'
p7.legend.label_text_font_size = '8pt'
p7.legend.location = 'top_left'

p8 = figure(plot_width=500, plot_height=300)
p8.line(x_axis, pr8[0], color='blue', legend=br8[0], line_width=2.5)
p8.line(x_axis, pr8[1], color='red', legend=br8[1], line_width=2.5)
p8.line(x_axis, pr8[2], color='green', legend=br8[2], line_width=2.5)
p8.line(x_axis, pr8[3], color='gold', legend=br8[3], line_width=2.5)
p8.line(x_axis, pr8[4], color='aqua', legend=br8[4], line_width=2.5)
p8.xaxis.axis_label = 'Quartos'
p8.legend.label_text_font_size = '8pt'
p8.legend.location = 'top_left'

p9 = figure(plot_width=500, plot_height=300)
p9.line(x_axis, pr9[0], color='blue', legend=br9[0], line_width=2.5)
p9.line(x_axis, pr9[1], color='red', legend=br9[1], line_width=2.5)
p9.line(x_axis, pr9[2], color='green', legend=br9[2], line_width=2.5)
p9.line(x_axis, pr9[3], color='gold', legend=br9[3], line_width=2.5)
p9.xaxis.axis_label = 'Quartos'
p9.legend.label_text_font_size = '8pt'
p9.legend.location = 'top_left'

grid = gridplot([[p1, p2, p3], [p4, p5, p6], [p7, p8, p9]])
show(grid)
# export_png(grid, filename='variacao.png', webdriver='firefox') """


""" from bokeh.plotting import figure, show, save
from bokeh.models import ColumnDataSource, LabelSet
x = [1, 2, 3, 4, 5]
prev = [23.5, 23.5, 23.5, 23.5, 23.5]
val = []
for i in range(5):
    val.append(previsao_preco('Centro', 1, 1, i+1, prev[i]))

val1 = variacao_preco(val)

p = figure(plot_width=400, plot_height=300)
p.line(x, val1, color='blue', line_width=2.5)
p.xaxis.axis_label = 'Quantidade de vagas'
p.yaxis.axis_label = 'Diferença'
show(p) """

# print(dataset['area'].mean())
