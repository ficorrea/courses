install.packages('randomForest', dependencies = T)
library(randomForest)

credito = read.csv(file.choose(), sep = ',', header = T)

modelo = randomForest(class ~., data = credito, ntree = 500)

# Resultados
modelo$predicted
modelo$importance
modelo$votes
modelo$forest
modelo$confusion

# Gráfico que exibe a variação de erro
plot(modelo)

predict(modelo, newdata = credito[163,])
