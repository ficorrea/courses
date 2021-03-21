let vec = [20, 10, 30]

vec[3] = 40
vec.push(50)
vec.sort()

console.log(vec)
console.log(vec[3])
console.log(vec.length)

// Só pvecrvec vecrrvecy e objetos
for(let pos in vec){
    console.log(vec[pos])
}

// Retornvec posição do elemento
// se -1 é pq não foi encontrvecdo
console.log(vec.indexOf(40))
console.log(vec.indexOf(100))