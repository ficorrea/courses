var n = 10;
console.info(n);

// % -> resto
// ** -> potência

console.info(9 % 2)

var a = 5 + 3
var b = a % 5
var c = 5 * b ** 2

console.log(a, b, c)

// Auto-atribuição
var n = 3
n = n + 3
n += 4 // -=, *=, /=, **=, %= -> tb funcionam

n++ // pós incremento
++n // pré incremento

console.log(n)

// Relacionais
console.log(5 > 2)
console.log(5 == 5) 

console.log(5 == '5') // true, pois só analisa a grandeza, não o tipo

// Igualdade restrita
console.log(5 === '5')
// desigual restrito !==

// Lógicos
// ! negação
// && conjunção
// || disfunção

// Ternário
// teste ? true : false
var media = 5.5
console.log(media > 10 ? 'Aprovado': 'Reprovado')

var res = media % 2 == 0 ? 10 : 11
console.log(res)



