// Maps
object maps {
  
  // Se chave duplicada, a última é validada
  val myMap: Map[Int, String] = 
    Map(19 -> "Felipe", 12 -> "Israel", 84 -> "Correia", 84 -> "Correa")
  
  val myMapMap = Map(22 -> "Lavinia", 7 -> "Correa")  
    
  def main(args: Array[String]){
    println(myMap)
    println(myMap(12))
    
    println(myMap.keys)
    println(myMap.values)
    
    myMap.keys.foreach { key =>
      println("key " + key)
      println("value " + myMap(key))      
    }    
    myMap.keys.foreach(println)
    myMap.values.foreach(println)
    
    println(myMap.contains(19))
    println(myMap ++ myMapMap)
    
  }
}