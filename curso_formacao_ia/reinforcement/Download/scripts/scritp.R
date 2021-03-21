#Formação Inteligência Artificial e Machine Learning

install.packages("ReinforcementLearning")

library(ReinforcementLearning)

ambiente <- gridworldEnvironment

print(ambiente)


estados <- c("s1", "s2", "s3", "s4")
acoes <- c("up", "down", "left", "right")


dados <- sampleExperience(N = 1000, env = ambiente, states = estados, actions = acoes)
head(dados)


modelo <- ReinforcementLearning(dados, s = "State", a = "Action", r = "Reward", 
                               s_new = "NextState", control =list(alpha = 0.1, gamma = 0.5, epsilon = 0.1))


modelo

policy(modelo)
