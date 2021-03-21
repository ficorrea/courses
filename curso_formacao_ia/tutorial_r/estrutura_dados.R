#### Vetores
x <- c(1,2,3,4,5,6)
# obrigatório uso do 'c' (combine) na sintaxe, para combinar os elementos
x
x[1]
x[3] <- 10
x[3]
y = c('a', 'b', 'c', 'd')
y
z = c(1L, 2L, 3L)
z

#### Matrizes
VADeaths
colnames(VADeaths)
rownames(VADeaths)

# só coluna
VADeaths[,1]

# só linha
VADeaths[1,]

# linhas de 1 a 3
VADeaths[1:3,]

#### Dataframe
longley
# obs acessa como matriz
# acessando coluna com $ ou nome
longley$Unemployed
longley['Unemployed']

#### Listas
ability.cov
ability.cov[1]
class(ability.cov$cov)
class(ability.cov$center)

# acesso elemento dentro da lista
ability.cov$cov[1:3,]

#### Fatores, variáveis categóricas com um número limitado de valores 
#### diferentes e são armazenados como inteiros
state.region
