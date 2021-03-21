// Higher-Order Functions
/* Funções capazes de receber outras funções
 * como argumento e retornar uma função
 */
object higherOrderFunctions {
  
  def math(x: Double, y: Double, f: (Double, Double) => Double): Double = f(x, y)
  
  def mathZ(x: Double, y: Double, z: Double, 
      f: (Double, Double) => Double): Double = f(f(x, y), z)
  
  def main(args: Array[String]){
    val res = math(10, 10, (x, y) => x + y)
    println(res)
    
    println(math(20, 30, (x, y) => x * y))
    println(math(20, 30, (x, y) => x min y))
    println(math(20, 30, (x, y) => x max y))
    println(math(20, 30, _+_))
    
    println(mathZ(20, 30, 10, (x, y) => x * y))
    println(mathZ(20, 30, 10, (x, y) => x min y))
    println(mathZ(20, 30, 10, (x, y) => x max y))
    println(mathZ(20, 30, 10, _*_))
    println(mathZ(20, 30, 10, _ max _))
  }  
}