import math 

# Binomial

def calc_coef_binomial(n, x):
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

def calc_binomial(n, x, p):
    coef = calc_coef_binomial(n, x)
    return coef*(p**x)*((1-p)**(n-x))

def calc_media(n, p):
    return n*p

def calc_var_dp(n, p):
    var = n*p*(1-p)
    return var, math.sqrt(var)

# Ex1.
a = calc_binomial(18, 2, 0.1)
print(a)

b = [calc_binomial(18, i, 0.1) for i in range(4, 19)]
print(sum(b))

c = [calc_binomial(18, i, 0.1) for i in range(3, 8)]
print(sum(c))

print(calc_media(18, 0.1))
print(calc_var_dp(18, 0.1))

# Ex2.
a = [calc_binomial(4, i, 0.2) for i in range(3)]
print(sum(a))

# Ex3.
a = [calc_binomial(20, i, 0.02) for i in range(0, 3)]
print(1 - sum(a))


# Poisson

def calc_poisson(lmd, x):
    return math.exp(-lmd)*lmd**x/math.factorial(x)

# Ex4.
a = calc_poisson(2.3, 2)
print(a)

# deveria ser >2 e <4 falhas pra dar o resultado esperado
b = [calc_poisson(2.3, i) for i in range(3, 4)]
print(sum(b))

c = calc_poisson(2.3*5, 10)
print(c)

# no mínimo 1 falha seria o mesmo que 1 - não ter falha
d = calc_poisson(2.3*2, 0)
print(1 - d)

# Ex5.
a = calc_poisson(0.1, 2)
print(a)

b = calc_poisson(0.1*10, 1)
print(b)

c = calc_poisson(0.1*20, 0)
print(c)

d = [calc_poisson(0.1*10, i) for i in range(2)]
print(1 - sum(d))

# Ex6.
a = calc_poisson(3, 0)
print(a)

b = [calc_poisson(3, i) for i in range(3)]
print(1 - sum(b))


print(calc_poisson(5*8, 50))
print(sum([calc_binomial(10, i, 0.3) for i in range(3, 6)]))
print(sum([calc_binomial(14, 13, 0.6), calc_binomial(14, 14, 0.6)]))

print(calc_binomial())