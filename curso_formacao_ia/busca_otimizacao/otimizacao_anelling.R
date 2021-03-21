install.packages("GenSA")

library(GenSA)

solucao = GenSA(fn = funcao, lower = c(-10,-10), upper = c(10,10), 
                control = list(verbose = TRUE))
solucao$par
solucao
