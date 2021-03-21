#Formação Inteligência Artificial e Machine Learning

#instalar e caregar pacote
install.packages("arules")
install.packages("arulesCBA")

#pacote secundário
install.packages("caret", dependencies=T)
library(caret)

tempo = read.csv(file.choose(), sep=";", header=T)
modelo = CBA(play ~ . , tempo, supp=0.05, conf=.9)
inspect(modelo$rules)

previsao = predict(modelo, tempo)
confusionMatrix(previsao,tempo$play)









