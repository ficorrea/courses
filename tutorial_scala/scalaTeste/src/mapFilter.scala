// map, flatMap, flatten e filter
object mapFilter {
  val myList = List(0, 1, 2, 3, 4, 5, 6)
  val myMap = Map(22 -> "lavinia", 7 -> "correa")
  def main(args: Array[String]){
    // map
    println(myList.map(_ * 2))
    println(myList.map(x => x + 2))
    println(myList.map(x => "hi" * x))
    println(myMap.map(x => "hi" + x))
    println(myMap.mapValues(x => "hi" + x))
    println("felipe".map(_.toUpper))
    
    // flatten
    println(List(List(0, 1, 2), List(0, 1, 2)).flatten)
    
    // flatMap
    println(myList.flatMap(x => List(x, x + 1)))
    
    // filter
    println(myList.filter(x => x % 2 == 0))
    println(myList.filter(x => x % 2 != 0))
  }
}