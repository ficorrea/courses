#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral

#install.packages("imager")

impressao <- function(d)
{

library(imager)


#image <- load.image(file.choose())
plot(image)


#coordenadas
x = c(18,53,88,122,158,192,227,262)


for (i in 1:8) {
  
  text(x[i],x[d[i]],"Q",cex=4,col = "red")
 
  
}

}

