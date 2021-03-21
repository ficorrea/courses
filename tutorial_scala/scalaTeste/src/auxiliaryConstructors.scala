// Class - Auxiliary Constructors

//          getter?   setter? 
// var      yes       yes
// val      yes       no
// default  no        no

class User(var name: String, var age: Int){
  
  def this(){
    this("Felipe", 33)
  }
  
  def this(name: String){
    this(name, 33)
  }
}

object auxiliaryConstructors {
  def main(args: Array[String]){
    var userNormal = new User("Felipe", 33)
    var user = new User()
    var userName = new User("Felipe")
  }  
}