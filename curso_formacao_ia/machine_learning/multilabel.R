install.packages('mlr', dependencies = T)
library(mlr)
library(caret)

# Dataset
musica = read.csv(file.choose(), sep=",", header = T)
head(musica)

# Transforma os valores binários em lógicos
musica[, 1:6] <- sapply(musica[, 1:6], as.logical)

# Guarda o nome dos rótulos das colunas
rotulos = colnames(musica)[1:6]

# Criação da tarefa
tarefa = makeMultilabelTask(data = musica, target = rotulos)

# Objeto de aprendizado
aprendizado = makeLearner("classif.rpart")

# Partição dos dados
particao = createDataPartition(1:592,p=.7)

# Descarrega caret para não ter conflito com método train
detach("package:caret", unload=TRUE)

# Modelo de Binary Relevance
tipoclass = makeMultilabelBinaryRelevanceWrapper(aprendizado)
modelo = train(tipoclass, tarefa, subset = particao$Resample1)
modelo

# Predição e resultados observando o hamming loss, que possui melhor performance quanto mais 
# próximo de 0
predicao = predict(modelo, task = tarefa, subset = subset(seq(1:592),!seq(1:592) %in% particao$Resample1))
predicao
performance(predicao, measures = list(multilabel.hamloss))

####################

# Modelo de Classifier Chains
tipoclass = makeMultilabelClassifierChainsWrapper(aprendizado)
modelo = train(tipoclass, tarefa, subset = particao$Resample1)

# Predição e resultados, observando o hamming loss
predicao = predict(modelo, task = tarefa, subset = subset(seq(1:592),!seq(1:592) %in% particao$Resample1))
performance(predicao, measures = list(multilabel.hamloss))
