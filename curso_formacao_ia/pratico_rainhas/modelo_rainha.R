library(GA)

# Algoritmo genético
resultado <- ga(type = "permutation", fitness = oitorainhas,
                lower = c(1,1,1,1,1,1,1,1), upper = c(8,8,8,8,8,8,8,8),
                popSize = 10, maxiter = 1000)

# Solução
summary(resultado)$solution

# Evolucao
plot(resultado)

# Impressão do resultado no tabuleiro
impressao(summary(resultado)$solution[1,])
