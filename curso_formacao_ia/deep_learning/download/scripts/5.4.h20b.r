#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral
#install.packages("h2o")
library(h2o)

# precisa ser inicializado
h2o.init()

#importa os dados de treino e teste
treino <- h2o.importFile(file.choose())
teste <- h2o.importFile(file.choose())

dim(treino)
head(treino)
colnames(treino)

#transforma a classe em factor - exigencia do funcionamento da rede neural profunda
treino[,785] <- as.factor(treino[,785])
teste[,785] <- as.factor(teste[,785])


modelo <- h2o.deeplearning(x = colnames(treino[,1:784]),  y = "C785",  training_frame = treino,  validation_frame = teste,  distribution = "AUTO",  activation = "RectifierWithDropout",  hidden = c(64,64,64),  sparse = TRUE, epochs = 20)

plot(modelo)

h2o.performance(modelo)


#previsao de novos dados
#vimos que na linha 20 tinha o numero 4
#vamos conferir
treino[20,785]

#fazendo previsão
pred <- h2o.predict(model, newdata = treino[20,1:784])

#verificando a previsão
pred$predict






