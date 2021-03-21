// Classes

// var      getter  setter
// val      getter  ------
// default  ------  ------
 
// Dependendo da declaração da variável
// pode a classe pode ser mutável ou não
class UserImtb(val name: String, val age: Int)
class UserMtb(var name: String, var age: Int)

class UserPrivate(private var name: String, val age: Int){
  def printName{println(name)}
}

class UserDefault(name: String, age: Int){
  def printName{println(name)}
  def printAge{println(age)}
}

object classes {
  def main(args: Array[String]){
    // Imutável
    var userImtb = new UserImtb("Felipe", 33)
    println(userImtb.name)
    println(userImtb.age)
    
    // Mutável
    var userMtb = new UserMtb("lavinia", 1)
    println(userMtb.name)
    println(userMtb.age)
    userMtb.name = "Lais"
    userMtb.age = 33
    println(userMtb.name)
    println(userMtb.age)
    
    // Privado
    var userPrivado = new UserPrivate("Samanta", 25)
    // println(userPrivado.name) -> erro de acesso
    userPrivado.printName
    println(userPrivado.age)
    
    // Default
    var userDefault = new UserDefault("Joao", 10)
    userDefault.printName
    userDefault.printAge
    
  }
}