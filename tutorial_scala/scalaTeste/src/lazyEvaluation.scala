// Lazy Evaluation

class strict{
  val s = {
    println("strict");
    9
  }
}

class lazyEval{
  lazy val l = {
    println("lazy");
    9
  }
}

object lazyEvaluation {
  def main(args: Array[String]){
    var s = new strict
    var l = new lazyEval
    println(s.s)
    println(l.l)
    
    val add = (a: Int, b: Int) => {
      println("Add");
      a + b
     }
    
    mtd1(add(5, 6))
    mtd2(add(5, 6))
    
   }
  
  def mtd1(n: Int){ 
    println("Mtd 1");
    println(n)
  }
  
  def mtd2(n: => Int){
    println("Mtd 2");
    println(n)
  }
}