#Formação Inteligencia Artificial e Machine Learning - Fernando Amaral
library(expert)



x <- list(	EXP1 <- list(	           INT <- c(650, 800, 850)),
           EXP2 <- list(	   INT <- c(500, 600, 700)),
           EXP3 <- list(	INT <- c(450, 650, 800)))


prob <- c(0.1, 0.5, 0.9)



#weights para o pesos "manuais"
inf <- expert(x, "weights", prob,  w=c(.1,.7,.2))

inf

hist(inf, col="blue")