pesos = c(1, 5, 10, 1, 7, 5, 1)
pontos = c(10, 20, 15, 2, 30, 10, 30)

fit <- function(x){
  
  pts = 0
  ps = 0
  
  for(i in 1:7){
    if (x[i] != 0){
      pts = pts + pontos[i]
      ps = ps +  pesos[i]
    }
  }
  if(ps > 15){
    pts = 0
  }
  return(pts)
}

mochila = ga('binary', fitness = fit, popSize = 10, 
             maxiter = 20, monitor = T, nBits = 7, 
             names = c("canivete", "feijao", "batatas", "lanterna", "saco de dormir", "corda", "bussola"))

summary(mochila)
summary(mochila)$solution
plot(mochila)
