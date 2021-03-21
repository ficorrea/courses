function soma(a=0, b=0){
    return a + b
}

function parimp(n){
    if (n % 2 == 0){
        return 'Par'
    } else {
        return 'Ímpar'
    }
}

let res = parimp(16)
console.log(res)

console.log(soma(7, 9))
console.log(soma(9))

let v = function mult(n){
    return n*9
}

console.log(v(3))

// Fatorial normal
function fat(n){
    let f = 1
    if (n == 0 || n == 1){
        return 1
    } else{
        for (c = n; c > 1; c--){
            f *= c  
        }
        return f
    }
}

console.log(fat(0))

// Recursiva
function recFat(n){
    if (n == 0 || n == 1){
        return 1
    } else {
        return n * recFat(n-1)
    }
}

console.log(recFat(0))