// If Else
object ifElse {
  def main(args: Array[String]){
    val x = 20
    val y = 30
    var r = ""
    
    if (x == 20){
      println("x == 20")
      r = "y == 30"
    }else{
      println("x != 20")
      r = "y != 30"
    }
    
    println(r)
    
    val res = if (x == 20) "x == 20" else "x != 20"
    println(res)
    
    println(if (y == 30) "y == 30" else "y != 30")
  }
}

// && and
// || or