// Lists
/* Não são mutáveis */
object lists {
  
  var myInts: List[Int] = List(1, 2, 3, 4, 5)
  var myNames = List("Felipe", "Israel", "Correa")
  
  def main(args: Array[String]){
    println(myInts)
    println(0 :: myInts)
    println(myInts)
    
    println(myNames)
    
    println(1 :: 5 :: 9 :: Nil)
    
    println(myNames.head)
    println(myNames.tail)
    
    println(myNames.isEmpty)
    
    println(myInts.reverse)
    
    // Lista normalizada
    println(List.fill(10)(8))
    
    println(myNames.max)
    println(myInts.min)
    
    // Iteração
    myInts.foreach(println)
    
    var sum = 0
    myInts.foreach(sum += _)
    
    for (name <- myNames){
      println(name)
    }
    
  }
}