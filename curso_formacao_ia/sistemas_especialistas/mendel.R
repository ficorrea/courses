library(expert)

# int = variável de interesse

x <- list( exp1 <- list(seed1 <- c(75, 80, 85), seed2 <- c(10, 15, 20), int <- c(650, 800, 850)),
           exp2 <- list(seed1 <- c(80, 90, 95), seed2 <- c(25, 30, 35), int <- c(500, 600, 700)),
           exp3 <- list(seed1 <- c(65, 70, 80), seed2 <- c(20, 25, 30), int <- c(450, 650, 800)))

prob <- c(0.1, 0.5, 0.9)
true_seed <- c(80, 25)

inf <- expert(x, 'ms', prob, true_seed)

# Resultados
inf
hist(inf, col = 'blue')

par(bg = 'white')
split.screen(c(2,2))
screen(1)
hist(inf,col = 'gray', main = 'Distribuição agregada')
screen(2)
s = density(x[[1]][[3]])
plot(s, main = 'Especialista 1')
polygon(s, col = 'blue')
screen(3)
s = density(x[[2]][[3]])
plot(s, main = 'Especialista 2')
polygon(s, col = 'blue')
screen(4)
s = density(x[[3]][[3]])
plot(s, main = 'Especialista 3')
polygon(s, col = 'blue')
close.screen(all = T)

summary(inf)
quantile(inf)
mean(inf)

dc = cdf(inf)
plot(dc)

og = ogive(inf)
plot(og)
