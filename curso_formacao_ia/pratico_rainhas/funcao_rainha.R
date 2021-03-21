oitorainhas <- function(solucao)
{
  
  # Inicializa um vetor com 64 posições preenchido com zeros
  vetor = rep.int(0,64)
  
  # Variável auxiliar
  posicao = 1
  
  # Transforma a solução em vetor com 64 posicoes
  for (i in 1:8) {
    vetor[ posicao + solucao[i] -1       ] = 1;
    posicao = posicao + 8
  }
  
  # Tranforma o vetor em uma matriz 8 x 8 
  queens = matrix(vetor, nrow=8,ncol=8,byrow =F)
  
  # Variável para contar os ataques
  total = 0 
  
  # Verifica ataques em linhas e colunas
  for (i in 1:8) {
    # Verifica colunas
    total = total + ifelse(sum(queens[,i])>1,1,0)
    # Verifica linhas
    total = total + ifelse(sum(queens[i,])>1,1,0)
  }
  
  # Faz a transposicao das diagonais
  tmp <- row(queens) - col(queens)
  z = split(queens,tmp)
  
  # Inverte a matriz para ler as outras diagonais
  queens2 = queens[,8:1]
  tmp <- row(queens2) - col(queens2)
  y = split(queens2,tmp)
  
  for (i in 1:15) {
    # Verifica diagonais
    total = total + ifelse(sum( z[[i]])>1,1,0)
    # Verifica diagonais inversa
    total = total + ifelse(sum( y[[i]])>1,1,0)
  }
  
  return(-total)
}