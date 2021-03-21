install.packages('rpart', dependencies = T)
library(rpart)
library(caret)

credito = read.csv(file.choose(), sep=",", header=T)

#criando samples de treino e teste
particao = createDataPartition(1:1000,p=.7)
creditotreino = credito[particao$Resample1,]
creditoteste = credito[- particao$Resample1,]

# Primeiro modelo sem alteração - outro metodo é anova para regressão
# O primeiro argumento define qual deve ser o atributo alvo e os atributos independentes
# O ~ fala que todos os outros atributos são independentes
modelo_1 = rpart(class  ~., data=creditotreino, method="class")

# Print do modelo
plot(modelo_1)
text(modelo_1)

# Predição e dados da previsão
previsao = predict(modelo_1, newdata=creditoteste)
previsao

# Transforma previsao em df e a coluna class em discreta
previsao = as.data.frame(previsao)
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")

# Matriz de confusao do pacote caret
# Correção para criação da matriz de confusão
previsao$class = as.factor(previsao$class)
confusionMatrix(previsao$class, creditoteste$class)

# Modelo 2
# Aqui o parâmetro control, define a quantidade mínima de elementos para ocorrer a divisão
modelo_2 = rpart(class  ~., data=credito, method="class", control=rpart.control(minsplit=20))
modelo_2

# Print modelo
plot(modelo_2)
text(modelo_2)

# Previsão e resultados
previsao = predict(modelo_2, newdata=creditoteste)
previsao = as.data.frame(previsao)
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")
previsao$class = as.factor(previsao$class)
confusionMatrix(previsao$class, creditoteste$class)


# Modelo 3 com poda, baseado no modelo 2
# O parâmetro cp, define o número para ocorrer a poda, se muito baixo, não ocorrerá divisão e se
# muito alto, praticamente não ocorrerá a poda
modelo_3 = prune(modelo_2, cp=0.05)
plot(modelo_3)
text(modelo_3)

# Previsão e resultados
previsao = predict(modelo_3, newdata=creditoteste)
previsao = as.data.frame(previsao)
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")
previsao$class = as.factor(previsao$class) 
confusionMatrix(previsao$class, creditoteste$class)
