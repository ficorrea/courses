// While Loop and Do While  
object whileLoopDo {
  def main(args: Array[String]){
    var x = 0
    
    while(x < 10){
      println("x -> " + x)
      x += 1
    }
    
    do{
      println("x -> " + x)
      x += 1
    } while (x <= 20)
  }
}