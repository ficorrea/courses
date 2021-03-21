#Formação Inteligência Artificial e Machine Learning - Fernando Amaral
#install.packages("tabuSearch")

library(tabuSearch)

z = tabuSearch(size = 12, iters = 1000, objFunc = compras, 
           listSize = 9, nRestarts = 10, repeatAll = 1, verbose = T)

plot(z)

summary(z)


summary(z, verbose = TRUE)
