install.packages('h2o', dependencies = T)
library(h2o)

options(warn=-1)

# Necessita inicialização
h2o.init()

# Importação dados de treino e teste
treino <- h2o.importFile(file.choose())
teste <- h2o.importFile(file.choose())

# Dimensões
dim(treino)
head(treino)
colnames(treino)

# Necessário transformar a classe em factor
# Exigência do funcionamento da rede neural profunda
treino[,785] <- as.factor(treino[,785])
teste[,785] <- as.factor(teste[,785])

# Criação do modelo
modelo <- h2o.deeplearning(x = colnames(treino[,1:784]),  y = "C785",  
                           training_frame = treino,  validation_frame = teste,  
                           distribution = "AUTO",  activation = "RectifierWithDropout",  
                           hidden = c(64,64,64),  sparse = TRUE, epochs = 20)

# Desempenho do treinamento
plot(modelo)

# Resultados
h2o.performance(modelo)

# Previsão de dados
treino[20,785] # -> dado encontrado na tabela
pred <- h2o.predict(modelo, newdata = treino[20,1:784])

# Resultado da predição
pred$predict
