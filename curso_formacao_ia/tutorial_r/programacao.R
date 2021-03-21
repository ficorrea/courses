a = 10
b = 20

#### IF/ELSE
if (a > 10){
  print('a > 10')
} else{
  print('a < 10')
}

x = ifelse(a>10, 'a > 10', 'a < 10')
x

#### FOR
for (i in 1:10){
  print(i)
}

#### WHILE
a = 1
while (a <= 10){
  print(a)
  a = a + 1
}

#### FUNÇÂO
par_impar <- function(numero){
  return(ifelse(numero%%2==0, 'Par', 'Impar'))
}

par_impar(13)
par_impar(44)
