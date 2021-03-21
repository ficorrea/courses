// Strings
object strings {
  
  val num = 25.5
  val str1: String = "Hello"
  val str2 = "World"
  
  def main(args: Array[String]){
    println(str1.length())
    println(str1.concat(str2))
    println(str1 + str2)
    
    // Printa os '()' extras no final por causa do
    // retorno da função
    val res = printf("(%f -- %s -- %s)", num, str1, str2)
    println(res)
    
    println("(%f -- %s -- %s)".format(num, str1, str2))
    printf("(%f -- %s -- %s)", num, str1, str2)
    
  }
}