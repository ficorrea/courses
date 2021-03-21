#Formação Inteligência Artificial e Machine Learning

#instalar e caregar pacote
install.packages("rpart")
library(rpart)

#pacote secundário
install.packages("caret", dependencies=T)
library(caret)

#importando dados
credito = read.csv(file.choose(), sep=",", header=T)

#criando samples de treino e teste
particao = createDataPartition(1:1000,p=.7)
creditotreino = credito[particao$Resample1,]
creditoteste = credito[- particao$Resample1,]



#primeiro modelo sem alteração - outro metodo é anova para regressão
modelo1 = rpart(class  ~., data=creditotreino, method="class")

#print no modelo para podermos comparar depois
plot(modelo1)
text(modelo1)


previsao = predict(modelo1, newdata=creditoteste)

#mostrar que previsao preve conforme a probabilidade 
previsao

#transforma previsao em df
previsao = as.data.frame(previsao)
#tranforma a coluna em discreta
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")

#matriz de confusao do pacote caret
confusionMatrix(previsao$class, creditoteste$class)

#novo modelo 
modelo2 = rpart(class  ~., data=credito, method="class", control=rpart.control(minsplit=20))
modelo2

#print no modelo para comparar depois
plot(modelo2)
text(modelo2)


previsao = predict(modelo2, newdata=creditoteste)
previsao = as.data.frame(previsao)
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")
confusionMatrix(previsao$class, creditoteste$class)


#poda
modelo3 = prune(modelo2, cp=0.05)
plot(modelo3)
text(modelo3)

previsao = predict(modelo3, newdata=creditoteste)
previsao = as.data.frame(previsao)
previsao$class = ifelse(previsao$bad >= .5, "bad", "good")
confusionMatrix(previsao$class, creditoteste$class)


