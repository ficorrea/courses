#Formação Inteligência Artificial e Machine Learning - Fernando Amaral

jogotictac <- function(jogada)
{

  
  verificavitoria = function()
  {
    #verifica vencedor
    decvit = paste(estadojogo,collapse="");   
    #horizontais
    if ( 
      (substr(decvit,1,3) %in% c("XXX","BBB"))   | ( substr(decvit,3,6) %in% c("XXX","BBB"))   | (substr(decvit,7,9) %in% c("XXX","BBB")) | 
      (paste(substr(decvit,1,1),substr(decvit,4,4),substr(decvit,7,7),sep="") %in% c("XXX","BBB")) |   # verticais
      (paste(substr(decvit,2,2),substr(decvit,5,5),substr(decvit,8,8),sep="") %in% c("XXX","BBB")) |
      (paste(substr(decvit,3,3),substr(decvit,6,6),substr(decvit,9,9),sep="") %in% c("XXX","BBB")) |
      (paste(substr(decvit,1,1),substr(decvit,5,5),substr(decvit,9,9),sep="") %in% c("XXX","BBB")) |  #transver
      (paste(substr(decvit,7,7),substr(decvit,5,5),substr(decvit,3,3),sep="") %in% c("XXX","BBB")) 
    )   warning("Vit?ria!")
  }
  
  
  

#reinicia o ambiente
if (jogada==0)
{
  
  #reinicia o estado do jogo
  estadojogo <<- c(replicate(9,"." ))
  #desenha a grade
  plot(0,type='n',axes=FALSE,ann=FALSE)
  abline(v=.87)
  abline(v=1.14)
  abline(h=-.34)
  abline(h=.32) 
 
  #IA joga primeiro aleatorio
  pj = sample(9,1)
  #pj = 4
  estadojogo[pj] <<- "X"
 
  
  
}
else
{
  
  #joga do humano
  #detecta jogada repetida do humano
  if (estadojogo[jogada] != "."  ) {
    stop("Jogada Ilegal!")
  }
  estadojogo[jogada] <<- "B"
  verificavitoria();
  
  
  #IA JOGA
  #Consulta o modelo em busca de sugest?o (policy)
  jogada =  modelottt$Policy[paste(estadojogo,collapse="")]
  jogada = as.integer(substr(jogada,2,2))
 
  
  #verifica se a sugest?o n?o veio vazia ou posi??o proibida, neste caso, joga na primeira op??o livre
  if (is.na(jogada) | estadojogo[jogada] != "." )
  {
    #registro da jogada sem policy
    
    print(paste0("Jogada ilegal: ", ifelse(is.na(jogada)," NA ", " Inv?lida, ")    ,paste(estadojogo,collapse="")))
    
    jogada = regexpr(".", paste0(estadojogo,collapse=""), fixed=T)[1]
    
  }
  
  #jogada de IA 
  estadojogo[jogada] <<- "X"
  
  verificavitoria()

}


#impressao
text(0.735,.8,labels=ifelse(estadojogo[1]=="."," ",estadojogo[1]),cex=7)
text(1,.8,labels=ifelse(estadojogo[2]=="."," ",estadojogo[2]),cex=7)
text(1.257,.8,labels=ifelse(estadojogo[3]=="."," ",estadojogo[3]),cex=7)
text(0.735,0,labels=ifelse(estadojogo[4]=="."," ",estadojogo[4]),cex=7)
text(1,0,labels=ifelse(estadojogo[5]=="."," ",estadojogo[5]),cex=7)
text(1.257,0,labels=ifelse(estadojogo[6]=="."," ",estadojogo[6]),cex=7)
text(0.735,-.73,labels=ifelse(estadojogo[7]=="."," ",estadojogo[7]),cex=7)
text(1,-.73,labels=ifelse(estadojogo[8]=="."," ",estadojogo[8]),cex=7)
text(1.257,-.73,labels=ifelse(estadojogo[9]=="."," ",estadojogo[9]),cex=7)


#detecta fim de jogo
fim = regexpr(".", paste0(estadojogo,collapse=""), fixed=T)[1]
if (fim==-1)
{
  warning("Fim de Jogo!")
  
}



}

