// String Interpolation
object stringInterpolation {
  def main(args: Array[String]){
    val name = "Felipe"
    val age = 33
    println(name + " tem " + age + " anos")
    println(s"$name tem $age anos")
    println(f"$name%s tem $age%d anos")
    println("felipe \nisrael")
    println(raw"felipe \nisrael")
    }
}