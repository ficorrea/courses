// Options Type
object options {
  
  val myList = List(0, 1, 2)
  val myMap = Map(22 -> "lavinia", 7 -> "correa")
  val opt: Option[Int] = Some(10)
  
  def main(args: Array[String]){
    
    // Retorna erro caso utilize somente get e 
    // não tiver valor None
    // O último get serve para buscar valor do Some()
    println(myList.find(_ > 10).get) 
    println(myList.find(_ > 10).getOrElse("nenhum valor"))
    
    println(myMap.get(7).get)
    println(myMap.get(7).getOrElse("nenhum valor"))
    
    println(opt.get)
    
  }
}