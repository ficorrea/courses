install.packages('ReinforcementLearning')
library(ReinforcementLearning)

# Definição do ambiente
ambiente <- gridworldEnvironment
ambiente

# Definição de estados e ações
estados <- c('s1', 's2', 's3', 's4')
acoes <- c('up', 'dowm', 'left', 'right')

# Criação do evento
dados <- sampleExperience(N = 1000, env = ambiente, 
                          states = estados, actions = acoes)
dados

# Criação do modelo
modelo <- ReinforcementLearning(dados, s = 'State', a = 'Action', 
                                r = 'Reward', s_new = 'NextState',
                                control = list(alpha = 0.001, gamma = 0.05, 
                                               epsilon = 0.1))

modelo
policy(modelo)

