#Formação Inteligência Artificial e Machine Learning - Fernando Amaral

install.packages("ReinforcementLearning")
library(ReinforcementLearning)


data_new <- sampleExperience(N = 1000, env = env, states = states, actions = actions, 
                             model = model, actionSelection = "epsilon-greedy", 
                             control = control)



control <- list(alpha = 0.2, gamma = 0.4, epsilon = 0.1)
modelottt <- ReinforcementLearning(tictactoe, s = "State", a = "Action", r = "Reward", 
                                   s_new = "NextState", iter = 2, control = control)
