// Object
let pessoa = {nome: 'Felipe', 
              sexo: 'M', 
              peso: 80, 
              engodar(p=0){
                  this.peso += p
                }}

// console.log(pessoa)
console.log(pessoa.nome)

console.log(pessoa.peso)
pessoa.engodar(2)
console.log(pessoa.peso)

