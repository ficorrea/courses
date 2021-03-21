#Formacao Inteligencia Artificial e Machine Learning

install.packages("FSelector", dependencies=T)
library(FSelector)


install.packages("e1071")
library(e1071)


install.packages("caret", dependencies=T)
library(caret)


anuncios = read.csv(file.choose(), sep=",",header=F)
head(anuncios)
dim(anuncios)


particao = createDataPartition(1:3279,p=.7)
anunciostreino = anuncios[particao$Resample1,]
dim(anunciostreino)
anunciosteste = anuncios[-particao$Resample1,]
dim(anunciosteste)


modelo = naiveBayes(V1559 ~. , data=anunciostreino)
previsao = predict(modelo, newdata=anunciosteste)
confusionMatrix(previsao, anunciosteste$V1559)



atributos <- chi.squared(V1559 ~., anuncios)

head(atributos)

subgrupo <- cutoff.k(atributos, 7)

subgrupo

modelo = naiveBayes(V1559 ~ V3 + V2 + V1 + V1244 + V1400 + V352 + V1345 , data=anunciostreino)
previsao = predict(modelo, newdata=anunciosteste)
confusionMatrix(previsao, anunciosteste$V1559)
