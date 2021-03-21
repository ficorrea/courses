#Formação Inteligência Artificial e Machine Learning - Fernando Amaral
compras <- function(solucao)
{
  
  #solucao = c(1,0,1,1,1,0,1,0,1,1,1,0)
  
  valores = c(1.1,1.2,1.25,1.41,1.5,1.63,2.05,2.22,2.65,2.9,3.04,3.16)
  
  

  soma = 0;
  produto = 1;
  
 
  
  for (i in 1:12) {
    if (solucao[i]==1)
    {
     soma = soma + valores[i];
     produto = produto * valores[i];
    }
  }
  
  if (soma==7.11 & produto==7.11)
  {
    return(7.11)
    
  }
  else
  {
       return(0)
  
    
  }  
  
}
