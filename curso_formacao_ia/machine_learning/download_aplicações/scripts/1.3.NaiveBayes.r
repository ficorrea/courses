#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral
install.packages("bnlearn")
library(bnlearn)


install.packages("caret", dependencies=T)
library(caret)


particao = createDataPartition(1:20000,p=.7)
segurotreino = insurance[particao$Resample1,]
seguroteste = insurance[- particao$Resample1,]
dim(segurotreino)
dim(seguroteste)

modelo = naive.bayes(x=segurotreino,training = "Accident")
modelo
plot(modelo)

previsao  = predict(modelo, seguroteste)
previsao
confusionMatrix(previsao, seguroteste$Accident)
