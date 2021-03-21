// Anonymous Function + Default values + No Return
object anonymousFunctionsMore{
  
  object Math{
    
    // Nome de função pode ser símbolo
    def +(x: Int, y: Int): Int = {
      return x + y
    }
    //def add(x: Int, y: Int) : Int = {
    //  return x + y
    //}
    
    // Função com valores default
    def add(x: Int = 10, y: Int = 10): Int = {
      return x + y
    }
  
    def **(x: Int) = x * x
    //def square(x: Int) = x*x
  }
  
  // Unit usado em funções sem retorno
  def print(x: Int, y: Int): Unit = {
    println(x + y)
  }
  
  def main(args: Array[String]){
    
    println(Math.+(2, 2))
    println(Math ** 2)
    println(Math.add())
    
    print(10, 10)
    
    // Função anônima 
    var add = (x: Int, y: Int) => x + y
    println(add(100, 100))
    
  }
}