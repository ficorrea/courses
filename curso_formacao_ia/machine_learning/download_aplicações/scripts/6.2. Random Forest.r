#Formação Inteligência Artificial e Machine Learning

install.packages("randomForest")
library(randomForest)


credito = read.csv(file.choose(), sep=",", header=T)

modelo = randomForest(class ~ ., data = credito, ntree=500 ) 


#previsao baseado nos dados out of bag
modelo$predicted
 
#importancia dos atributos no modelo
modelo$importance
 
#proporção de votos na classificação de cada instancia
modelo$votes
 
#arvores induzidas
modelo$forest

#matriz de confusão baseado nos dados out of bag
modelo$confusion
 
plot(modelo)
 
#fazendo previsões com um registro
predict(modelo, newdata = credito[154,])