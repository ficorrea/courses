#Formacao Inteligencia Artificial e Machine Learning - Fernando Amaral
#warnb
options(warn=-1)

#importa arquivos de digitos, importar treino
digitos <- read.csv(gzfile(file.choose()), header=F)

# cada linha possui 785 colunas, são 784 pixels e mais uma coluna para a classe (digito)
dim(digitos)
head(digitos)


# visualizar 4 digitos compartilhando a tela
split.screen(figs=c(2,2))

#precisamos transformar a imagem que esta na linha em uma matriz de duas dimensões
#784 é 28 x 28, ou seja, uma imagem de 28 x 28 pixels

dig = t(matrix(unlist(digitos[20,-785]), nrow = 28, byrow = F))
dig = t(apply(dig, 2, rev))

#ver imagem em "pixels"
dig

screen(1)
image(dig, col = grey.colors(255))

#conferindo se é o digito 4
digitos[20,785]

screen(2)
dig = t(matrix(unlist(digitos[2,-785]), nrow = 28, byrow = F))
dig = t(apply(dig, 2, rev))
image(dig,col=grey.colors(255))

screen(3)
dig = t(matrix(unlist(digitos[4,-785]), nrow = 28, byrow = F))
dig = t(apply(dig, 2, rev))
image(dig,col=grey.colors(255))

screen(4)
dig = t(matrix(unlist(digitos[5,-785]), nrow = 28, byrow = F))
dig = t(apply(dig, 2, rev))
image(dig,col=grey.colors(255))

close.screen(all=TRUE)




													 
													 
