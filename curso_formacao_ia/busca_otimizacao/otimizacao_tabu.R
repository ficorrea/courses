install.packages('tabuSearch', dependencies = TRUE)

library(tabuSearch)

solucao = tabuSearch(size = 12, iters = 1000, objFunc = compras, 
               listSize = 9, nRestarts = 10, repeatAll = 1, 
               verbose = TRUE)

plot(solucao)
summary(solucao)

solucao$configKeep[299,]
summary(solucao, verbose=TRUE)
