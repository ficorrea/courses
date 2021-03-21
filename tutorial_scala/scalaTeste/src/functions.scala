// Functions
object functions {
  
  object Math{
    
    def add(x: Int, y: Int) : Int = {
      return x + y
    }
    
    def square(x: Int) = x*x
  }
  
  def add(x: Int, y: Int): Int = {
    return x + y
  }
  
  // Somente uma linha o retorno fica implícito
  def sub(x: Int, y: Int): Int = {
    x - y
  }
  
  def mul(x: Int, y: Int): Int = x * y
  
  def div(x: Int, y: Int) = x / y
 
  def main(args: Array[String]){
    // Possibilidades de invocação da função
    println(Math.add(2, 2))
    println(Math square 2)
    println(add(2, 2))
    println(sub(2, 2))
    println(mul(2, 2))
    println(div(2, 2))
  }
}