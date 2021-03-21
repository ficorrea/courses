#Formação Inteligência Artificial e Machine Learning
install.packages("bnlearn")
library(bnlearn)


install.packages("caret", dependencies=T)
library(caret)


res <- hc(insurance)
plot(res)


modelo <- bn.fit(res, data = insurance)
modelo$GoodStudent



cpquery(modelo, event =( Accident=="Moderate" | Accident=="Severe" ), 
        evidence=(Age=="Senior" & RiskAversion=="Adventurous" & MakeModel == "SportsCar"))


