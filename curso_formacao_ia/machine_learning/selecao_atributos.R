install.packages('FSelector', dependencies = T)
library(FSelector)
library(e1071)
library(caret)

# Dataset
anuncios = read.csv(file.choose(), sep=",",header=F)
head(anuncios)
dim(anuncios)

# Split dos dados em teste e treino
particao = createDataPartition(1:3279,p=.7)
anunciostreino = anuncios[particao$Resample1,]
dim(anunciostreino)
anunciosteste = anuncios[-particao$Resample1,]
dim(anunciosteste)

# Modelo com todos os atributos e resultado
modelo = naiveBayes(V1559 ~. , data=anunciostreino)
previsao = predict(modelo, newdata=anunciosteste)
confusionMatrix(previsao, anunciosteste$V1559)

# Seleção dos atributos mais relevantes, utilizando chi-squared
atributos <- chi.squared(V1559 ~., anuncios)
head(atributos)

# Escolha dos atributos mais importantes, a quantidade é definida pelo parâmetro k
subgrupo <- cutoff.k(atributos, k = 7)
subgrupo

# Modelo com os atributos mais importantes definidos
modelo = naiveBayes(V1559 ~ V3 + V2 + V1 + V1244 + V1400 + V352 + V1345 , data=anunciostreino)
previsao = predict(modelo, newdata=anunciosteste)
confusionMatrix(previsao, anunciosteste$V1559)
