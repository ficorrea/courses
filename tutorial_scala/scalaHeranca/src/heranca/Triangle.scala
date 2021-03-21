package heranca

class Triangle(var width: Double, var height: Double) 
extends Polygon with Shape{
  // Override para sobrescrever a função
  // herdada de Polygon
  override def area: Double = (width * height / 2)
  def color: String = "green"
}