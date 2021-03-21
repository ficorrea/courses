install.packages('neuralnet', dependencies = T)
library(neuralnet)
library(caret)

# Cópia do dataset
myiris = iris

# Binarização das classes (dummy variables)
myiris = cbind(myiris,myiris$Species=='setosa')
myiris = cbind(myiris,myiris$Species=='versicolor')
myiris = cbind(myiris,myiris$Species=='virginica')

# Renomeação das colunas
names(myiris)[6] <- 'setosa'
names(myiris)[7] <- 'versicolor'
names(myiris)[8] <- 'virginica'

# Visualização do dataset
summary(myiris)

# Partição do dataset entre treino e teste
particao = createDataPartition(1:dim(myiris)[1],p=.7)
iristreino = myiris[particao$Resample1,]
iristeste = myiris[- particao$Resample1,]
dim(iristreino)
dim(iristeste)

# Criação do modelo
modelo = neuralnet( setosa  + versicolor  +  virginica  ~ Sepal.Length + Sepal.Width +  Petal.Length + Petal.Width , iristreino, hidden=c(3,4,5))

# Visualização da rede neural
plot(modelo)

# Predição dos de teste no modelo
teste = compute(modelo,iristeste[,1:4])

# Resultados
teste$net.result

# Manipulação dos resultados para visualização na matrix de confusão
resultado = as.data.frame(teste$net.result)

names(resultado)[1] <- 'setosa'
names(resultado)[2] <- 'versicolor'
names(resultado)[3] <- 'virginica'

resultado$class = colnames(resultado[,1:3])[max.col(resultado[,1:3], ties.method = 'first')]

confusao = table(resultado$class,iristeste$Species)
confusao

# Acurácia
sum(diag(confusao) * 100 / sum(confusao))
