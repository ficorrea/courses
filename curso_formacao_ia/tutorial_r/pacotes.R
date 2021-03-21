setRepositories()
# Opção que revolveu o problema de instalação das libs
options(repos='http://cran.rstudio.com/')


install.packages("e1071", dependencies = TRUE)
library(e1071)

