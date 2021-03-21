// Sets
/* Coleção de diferentes elementos 
 * de mesmo tipo 
 */
object sets {
  
  // Set é por default imutável, declaração abaixo para
  // torná-la mutável
  var mySet = scala.collection.mutable.Set(0, 1, 2, 3)
  val mineSet: Set[Int] = Set(1, 2, 3, 4, 4, 5, 5, 6, 6) 
  
  def main(args: Array[String]){
    // Sets não possuem index, portanto 
    // o comando abaixo é pra verificar
    // a presença de um elemento
    println(mineSet(10))
    
    // Inserção temporária
    println(mySet + 10)
    println(mySet)
    
    // Concatenação
    println(mySet ++ mineSet)
    println(mySet.++(mineSet))
    
    // Interseção
    println(mySet & mineSet)
    println(mySet.&(mineSet))
    println(mySet.intersect(mineSet))
    
    mySet.foreach(println)
    
    for (num <- mySet){
      println(num)
    }
    
  }
}