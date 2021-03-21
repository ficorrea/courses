// Partially Applied Functions

import java.util.Date

object partiallyAppliedFunctions {
  
  def log(date: Date, message: String){
    println(date + " : " + message)
  }
  
  def main(args: Array[String]){
  
    val sum = (x: Int, y: Int, z: Int) => x + y + z
    println(sum(10, 20, 30))
    
    // Função Parcial
    val f = sum(10, _: Int, _: Int)
    println(f(20, 30))
    
    val date = new Date
    val newLog = log(date, _: String)
    newLog("Message 1")
    newLog("Message 2")
    newLog("Message 3")
    newLog("Message 4")    
  }
}