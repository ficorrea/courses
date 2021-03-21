#Formacao Inteligencia Artificial e Machine Learning. Fernando Amaral
#carrega os dados de distancia, que devem ser baixados do site
mapa =read.csv(file.choose(), header=T, sep=";", row.names = c("Linden","Parika","Lethem","Rosignol","New Amsterdam"))
library(GA)
#funcao de adaptacao
f <-function(z) {
dist = 0
for (i in 1:4)
{
 cidade1 = z[i]
 cidade2 = z[i+1]
 dist = dist + mapa[cidade1, cidade2]
}
return(-dist)
}

#algoritmo genetico
resultado <- ga(type="permutation", fitness=f,min=c(1,1,1,1,1), max=c(5,5,5,5,5),popSize = 10, maxiter = 5000, names=c("Linden","Parika","Lethem","Rosignol","New Amsterdam"))

#solucao
summary(resultado)$solution

#evolucao
plot(resultado)
