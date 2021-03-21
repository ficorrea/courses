install.packages('GA', dependencies = TRUE)
library(GA)

fit <- function(x){
  
  resultado = 2 * x  + 5
  
  if(resultado > 30){
    return(30 - resultado)
  }else{
    return(resultado - 30)
  }
}

valor = ga('real-value', fitness = fit, lower = -20, upper = 20, 
           popSize = 15, maxiter = 100, monitor = T, names = ('x'))

summary(valor)$solution
plot(valor)
