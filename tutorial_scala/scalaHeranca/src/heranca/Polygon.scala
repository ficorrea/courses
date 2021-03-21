package heranca

//class Polygon {
//  def area: Double = 0.0
//}

// Recebe o nome de trait para poder
// ser herdada por uma subclasse que
// já herda de outra superclasse
trait Shape{
  def color: String
}

// Classe abstrata
abstract class Polygon{
  def area: Double
}

object Polygon{
  def main(args: Array[String]){
    //var poly = new Polygon
    //printArea(poly)
    
    var rect = new Rectangle(25.0, 10.0)
    printArea(rect)
    rect.printHeigth
    rect.printWidth
    println(rect.color)
    
    var trgl = new Triangle(12.0, 16.0)
    printArea(trgl)   
    println(trgl.color)
    
  }
  
  def printArea(p: Polygon){
    println(p.area)
  }
  
}

// Quando superclass abstrata, subclasses
// não precisam do "override" para função 
// abstrata