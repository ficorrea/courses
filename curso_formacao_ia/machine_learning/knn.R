install.packages('class', dependencies = T)
library(class)

iris_teste = iris
new_iris = iris_teste[1,]
iris_train = iris_teste[-1,]

dim(new_iris)
dim(iris_train)

new_iris$Species

previsao = knn(iris_train[,1:4], new_iris[,1:4], iris_train[,5], k = 3)
previsao
