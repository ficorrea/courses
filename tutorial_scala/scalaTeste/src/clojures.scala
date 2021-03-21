// Clojures
 /* Função que utiliza uma ou mais 
  * variáveis declaradas externamente
  * a si
  */
object clojures {
  
 // Se "var" a última atribuição que vale
 //var number = 10
 val number = 10
  
 val add = (x: Int) => x + number  
  
 def main(args: Array[String]){
   //number = 100;
   println(add(20))
   println(number)
 } 
}