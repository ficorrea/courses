#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral
#install.packages("neuralnet")
library(neuralnet)

myiris = iris

myiris = cbind(myiris,myiris$Species=='setosa')
myiris = cbind(myiris,myiris$Species=='versicolor')
myiris = cbind(myiris,myiris$Species=='virginica')

names(myiris)[6] <- 'setosa'
names(myiris)[7] <- 'versicolor'
names(myiris)[8] <- 'virginica'

summary(myiris)

#install.packages("caret", dependencies=T)
library(caret)

#particao
particao = createDataPartition(1:dim(myiris)[1],p=.7)
iristreino = myiris[particao$Resample1,]
iristeste = myiris[- particao$Resample1,]
dim(iristreino)
dim(iristeste)

modelo = neuralnet( setosa  + versicolor  +  virginica  ~ Sepal.Length + Sepal.Width +  Petal.Length + Petal.Width , iristreino, hidden=c(5,4))

print(modelo)
plot(modelo)

teste = compute(modelo,iristeste[,1:4])

teste$net.result

resultado = as.data.frame(teste$net.result)

names(resultado)[1] <- 'setosa'
names(resultado)[2] <- 'versicolor'
names(resultado)[3] <- 'virginica'

resultado$class = colnames(resultado[,1:3])[max.col(resultado[,1:3], ties.method = 'first')]

confusao = table(resultado$class,iristeste$Species)
confusao

#Acertos
sum(diag(confusao) * 100 / sum(confusao))



















