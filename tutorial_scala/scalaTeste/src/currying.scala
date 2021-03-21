// Currying
/* Técnica que transforma uma função
 * que necessita de vários argumentos
 * em uma que necessite de somente
 * um argumento
 */
object currying {
  
  def add(x: Int, y: Int) = x + y
  
  // Exemplos de currying
  def add2(x: Int) = (y: Int) => x + y
  def add3(x: Int) (y: Int) = x + y
  
  def main(args: Array[String]){
    println(add(10, 20))
    
    val sumAdd2 = add2(50)
    println(sumAdd2(50))
    
    // Para este caso necessita sinalizar 
    // a segunda variável através do '_'
    val sumAdd3 = add3(50)_
    println(sumAdd3(50))
  }
  
}