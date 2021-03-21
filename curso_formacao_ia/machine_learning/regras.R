install.packages(c('arules', 'arulesCBA'), dependencies = T)
library(arules)
library(arulesCBA)
library(caret)

tempo = read.csv(file.choose(), sep = ';', header = T)

# Criação do modelo
modelo = CBA(play ~., tempo, support = 0.05, confidence = 0.9)

# Verificar regras
inspect(modelo$rules)

# Resultados
previsao = predict(modelo, tempo)
head(previsao)
confusionMatrix(previsao, tempo$play)
