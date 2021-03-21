#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral

#install.packages("GA")
library(GA)


#algoritmo genetico
resultado <- ga(type="permutation", fitness=oitorainhas,min=c(1,1,1,1,1,1,1,1), max=c(8,8,8,8,8,8,8,8),popSize = 10, maxiter = 1000)

#solucao
summary(resultado)$solution

#evolucao
plot(resultado)

impressao(summary(resultado)$solution[1,])

