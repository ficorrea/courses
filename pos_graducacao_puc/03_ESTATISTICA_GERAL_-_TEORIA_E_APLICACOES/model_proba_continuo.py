import math

# Exponencial
# Deve estar explícito 1/alfa para entrar na fórmula

def calc_exp(alfa, a, b):
    return math.exp(-(alfa)*a) - math.exp(-(alfa)*b)

a = calc_exp(1/1000, 0, 1000)
print(a)

b = calc_exp(1/1000, 900, 1200)
print(b)

c = calc_exp(1/1000, 0, 850)
print(1 - c)

# Ex1.
a = calc_exp(1/1000, 0, 1000)
print(a)

# print(math.exp(-(1/1000)*0))


# Ex2.
A = 1 - calc_exp(1/80, 0, 100)
B = 1 - calc_exp(1/100, 0, 100)
print((A * 0.7) + (B * 0.3))

print(calc_exp(3, 0, 1))
