#Formacao Inteligencia Artificial e Machine Learning

install.packages("mlr")
library(mlr)

install.packages("caret", dependencies=T)
library(caret)

musica = read.csv(file.choose(), sep=",", header = T)

head(musica)

musica[, 1:6] <- sapply(musica[, 1:6], as.logical)

rotulos = colnames(musica)[1:6]

#criamos a tarefa 
tarefa = makeMultilabelTask(data = musica, target = rotulos)
#cria um objeto de aprendizado
aprendizado = makeLearner("classif.rpart")

#primeiro binary relevance
tipoclass = makeMultilabelBinaryRelevanceWrapper(aprendizado)

#cria particao de dados
particao = createDataPartition(1:592,p=.7)

#descarrega caret para não ter conflito com método train
detach("package:caret", unload=TRUE)

#treina o modelo
modelo = train(tipoclass, tarefa, subset = particao$Resample1)
modelo

#fazemos a previsao
predicao = predict(modelo, task = tarefa, subset = subset(seq(1:592),!seq(1:592) %in% particao$Resample1))
predicao


#avaliar a performance e anotar o resultado
performance(predicao, measures = list(multilabel.hamloss))

####################
#testando outro tipo de transformação
#classifier chains
tipoclass = makeMultilabelClassifierChainsWrapper(aprendizado)

#treina o modelo
modelo = train(tipoclass, tarefa, subset = particao$Resample1)

#fazemos a previsao
predicao = predict(modelo, task = tarefa, subset = subset(seq(1:592),!seq(1:592) %in% particao$Resample1))

#avaliar a performance e anotar o resultado
performance(predicao, measures = list(multilabel.hamloss))