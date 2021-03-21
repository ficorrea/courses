install.packages('fpc', dependencies = T)
install.packages('cluster', dependencies = T)
library(fpc)
library(cluster)

cls = kmeans(iris[,1:4], centers = 3)
cls$cluster
cls$centers

# Matriz de confusão
table(iris$Species, cls$cluster)

# Visualização
plotcluster(iris[,1:4], cls$cluster)
clusplot(iris[,1:4], cls$cluster)
plot(iris[,3:4], col = iris$Species, pch = cls$cluster)
