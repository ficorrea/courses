// Arrays

import Array._

object arrays {
  
  val array1:  Array[Int] = new Array[Int](4)
  val array2 = new Array[String](2)
  val array3 = Array(0, 1, 2, 3, 4)
  
  def main(args: Array[String]){
    array1(0) = 10
    array1(1) = 20
    array1(2) = 30
    array1(3) = 40
    
    for (x <- array1){
      println(x)
    }
     
    array2(0) = "a"
    array2(1) = "b"
    //array2(2) = "c" -> Erro de out of bounds
    
    // Imprimir como lista
    val res = concat(array1, array3)
    println(res.toList.sorted)
    
    
    for (i <- 0 to (array3.length - 1)){
      println(i)
    }
  }
}