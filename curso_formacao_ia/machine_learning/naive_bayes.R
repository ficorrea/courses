# Pacote de redes bayesianas
install.packages('bnlearn', dependencies = T)

# Pacote que gera a matrix de confusão
install.packages('caret', dependencies = T)

# Pacotes solicitados pelo caret
install.packages('lattice', dependencies = T)
install.packages('ggplot2', dependencies = T)

library(bnlearn)
library(caret)

particao = createDataPartition(1:20000,p=.7)
segurotreino = insurance[particao$Resample1,]
seguroteste = insurance[- particao$Resample1,]
dim(segurotreino)
dim(seguroteste)

modelo = naive.bayes(x = segurotreino, training = 'Accident')
modelo
plot(modelo)

previsao = predict(modelo, seguroteste)
previsao
confusionMatrix(previsao, seguroteste$Accident)
