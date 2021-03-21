install.packages('arulesViz', dependencies = T)
library(arules)
library(arulesViz)

transacoes = read.transactions(file.choose(), format = 'basket', sep = ',')
transacoes
inspect(transacoes)
image(transacoes)

# Modelo
# Em parâmetros são definidos os valores mínimos de suporte, confiança e tamanho de transação
regras = apriori(transacoes, parameter = list(supp = 0.03, conf = 0.4, minlen = 2))
regras
summary(regras)
inspect(regras)

# Visualização
plot(regras, method = 'graph')
plot(regras, method = 'matrix')
plot(regras, method = 'matrix', engine = '3d', measure = 'lift', control = list(reorder = 'support'))
plot(regras, method = 'grouped')
