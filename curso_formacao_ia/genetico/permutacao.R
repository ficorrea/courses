data = read.csv(file.choose(), header=T, sep=";")

fit <-function(z) {
  dist = 0
  for (i in 1:4)
  {
    cidade1 = z[i]
    cidade2 = z[i+1]
    dist = dist + data[cidade1, cidade2]
  }
  return(-dist)
}

caminho <- ga(type="permutation", fitness=fit, min=c(1,1,1,1,1), 
              max=c(5,5,5,5,5), popSize = 10, maxiter = 1000, 
              names=c("Linden","Parika","Lethem","Rosignol","New Amsterdam"))

summary(caminho)
summary(caminho)$solution
plot(caminho)


