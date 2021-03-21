// Reduce, fold and scan
object reduceFoldScan {
  val myList = List(1, 2, 3, 4, 5, 6)
  val myStr = List("A", "B", "C")
  def main(args: Array[String]){
    // Reduce
    println(myList.reduceLeft(_ + _))
    println(myList.reduceLeft((x , y) => {println(x + " , " + y); x + y}))
    println(myList.reduceRight((x , y) => {println(x + " , " + y); x - y}))
    
    // Fold
    println(myList.foldLeft(30)(_ * _))
    println(myStr.foldLeft("f")(_ + _))
    println(myStr.foldRight("f")(_ + _))
    
    // Scan
    println(myList.scanLeft(30)(_ * _))
    println(myStr.scanLeft("f")(_ + _))
    
  }
}