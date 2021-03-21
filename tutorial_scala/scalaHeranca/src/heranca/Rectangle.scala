package heranca

class Rectangle(var width: Double, var height: Double) 
extends Polygon with Shape{
  
  def area: Double = width * height
  
  def printWidth{
    println(width)
  }
  
  def printHeigth{
    println(height)
  }
  
  def color: String = "blue"
}