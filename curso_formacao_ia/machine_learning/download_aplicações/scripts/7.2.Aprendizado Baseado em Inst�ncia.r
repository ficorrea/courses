#Formação Inteligência Artificial e Machine Learning

#instalar e caregar pacote
install.packages("class")
library(class)


novairis = iris
iristeste = novairis[1,]
novairis = novairis[-1,]
dim(iristeste)
dim(novairis)
iristeste$Species


previsao = knn(novairis[,1:4],iristeste[,1:4],novairis[,5],k=3)
previsao

