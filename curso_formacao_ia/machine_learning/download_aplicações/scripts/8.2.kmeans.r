#Formação Inteligência Artificial e Machine Learning

install.packages("fpc")
library(fpc)

install.packages("cluster")
library(cluster)


cls = kmeans(iris[,1:4],centers=3)
cls$cluster
cls$centers

table(iris$Species, cls$cluster)


plotcluster(iris[1:4],cls$cluster)
clusplot(iris[1:4],cls$cluster)


plot(iris[,3:4], col=iris$Species, pch=cls$cluster)
