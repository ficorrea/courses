// Tuples 
/* Contem elementos 
 * de tipos diferentes
 */

// Armazenam outras tuplas
object tuples {
  
  // São imutáveis
  val myTuple = ("felipe", 33, 22, false)
  
  // Tuplas declaradas desta forma só possuem 
  // até 22 elementos 
  val myTuple2 = new Tuple2(1, "lavinia")
  
  def main(args: Array[String]){
    println(myTuple._1) // Notação gerada 
    println(myTuple._2) // automaticamente
    println(myTuple._3)
    println(myTuple._4)
    
    myTuple.productIterator.foreach{
      i => println(i)
    }
    myTuple2.productIterator.foreach(println)
    
    // Notação que cria uma tupla,
    // mas é válida somente para
    // 2 elementos
    println(1 -> "correa")
    
  }
  
}