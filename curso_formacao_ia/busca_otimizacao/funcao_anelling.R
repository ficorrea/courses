funcao <- function(dados){
  
  x = dados[1]
  y = dados[2]
  
  return ((1-x)^2 + 100 * (y - x^2)^2)
  
}