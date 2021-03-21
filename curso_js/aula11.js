// Condição simples
var vel = 60.5
console.log(`A velocidade é ${vel}km/h`)
if (vel > 60){
    console.log(`Multado`)
}
console.log(`Dirija bem...`)

// Condição múltipla
var pais = 'Brasil'
if (pais === 'Brasil'){
    console.log('Você é brasileiro!')
} else{
    console.log('Você é estrangeiro!')
}

// Condição aninhada
var idade = 19
console.log(`Você tem ${idade} anos.`)
if (idade < 16){
    console.log('Não vota')
} else if (idade < 18 || idade >= 65){
    console.log('Voto opcional')
} else{
    console.log('Voto obrigatório')
}

// Time
var data = new Date()
console.log(data.getFullYear())

// Switch / Case (break é obrigatório)
switch(data.getDay()){
    case 0:
        console.log('Domingo')
        break
    case 1:
        console.log('Segunda')
        break
    case 2:
        console.log('Terça')
        break
    case 3:
        console.log('Quarta')
        break
    case 4:
        console.log('Quinta')
        break
    case 5:
        console.log('Sexta')
        break
    case 6:
        console.log('Sábado')
        break 
    default:
        console.log('Dia inexistente!!!')
        break // break opcional      
}