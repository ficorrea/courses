#Formação Inteligência Artificial e Machine Learning

install.packages("arules")
library(arules)

install.packages("arulesViz")
library("arulesViz")


transacoes = read.transactions(file.choose(), format="basket",  sep=",")
transacoes 
inspect(transacoes) 
image(transacoes)



regras = apriori(transacoes, parameter=list(supp=0.03,conf=0.4,minlen=2))
regras
summary(regras)
inspect(regras) 

plot(regras, method="graph")
plot(regras, method="matrix")
plot(regras, method="matrix",engine="3d", measure="lift", control=list(reorder=TRUE))
plot(regras, method="grouped")