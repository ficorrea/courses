// Match Expressions
object matchExpressions {
   def main(args: Array[String]){
     
     val age = 100;
     
     age match{
       case 10 => println(age)
       case 20 => println(age)
       case 30 => println(age)
       case _ => println("default")
     }
     
     val result = age match{
       case 10 => age
       case 20 => age
       case 30 => age
       case _ => "default"
       
     }
     
     println("result = " + result)
  }
  
   val i = 7
   
   i match{
     case 1 | 3 | 5 | 7 | 9 => println("odd")
     case 2 | 4 | 6 | 8 | 10 => println("even")
   }
   
}