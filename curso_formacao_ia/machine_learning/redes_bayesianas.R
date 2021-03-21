library(bnlearn)
library(caret)

res <- hc(insurance)
plot(res)

modelo <- bn.fit(res, data = insurance)
modelo$Age

cpquery(modelo, event = (Accident == 'Moderate' | Accident == 'Severe'),
        evidence = (Age == 'Senior' & RiskAversion == 'Adventurous' & MakeModel == 'SportsCar'))


# Neste caso não ocorreu a separação em teste e treino, pois o objetivo é verificar 
# a probabilidade de certo evento ocorrer.