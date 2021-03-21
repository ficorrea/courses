// For Loop
object forLoop {
  def main(args: Array[String]){
    
    for (i <- 0 to 1; j <- 0 to 1; l <- 0 to 1; n <- 0 to 1){
      println(i,j,l,n)
    }
    
    for (i <- 1.to(15)){
      println(i)
    }
    
    for (i <- 1 until 10){
      println(i)
    }
    
    val list = List(1, 15, 10, 12, 6, 8, 7, 9, 3)
    
    for (i <- list){
      println(i)
    }
    
    for (i <- list if i < 9){
      println(i)
    }
    
    for {i <- list if i > 6} yield{
      println(i * i)
    }
    
    var res = for {i <- list if i > 6} yield{
      i * 3
    }
    
    println(res)
  }

}