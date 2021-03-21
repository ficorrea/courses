# Verificar diretório padrão
getwd()

# Setar diretório
setwd("/home/felipe/Documents/curso_formacao_ia/tutorial_r")

# Sair
quit()

# Verifica o tipo do objeto
class(iris)

# Salvar e carregar objetos
save(objetos, file = "nome")
# ***objetos = variáveis
# *** nome = caminho diretório
load(file = "nome")

iris_teste = iris
save(iris_teste, file = "iris_teste.Rdata")
# Remove objetos da memória
rm(iris_teste)
load(file = "iris_teste.Rdata")
iris_teste

# Visualização de dados
plot()
hist()
boxplot()

x = c(12, 34, 56, 79)
y = c(1, 6, 9, 14)
plot(x,y)



