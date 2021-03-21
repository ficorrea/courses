import numpy as np

# Array
a = np.array([1, 2, 3])
np.log(a)
np.exp(a)

# Dot
a = np.array([1, 2])
b = np.array([2, 1])
a*b
(a*b).sum()
np.dot(a, b)
a.dot(b)
np.sqrt(a.dot(a))  # Magnitude

# Loop List or numpy array
from datetime import datetime

a = np.random.randn(100)
b = np.random.randn(100)
T = 100000


def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b):
        result += e*f
    return result


t0 = datetime.now()
for t in range(T):
    slow_dot_product(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt2 = datetime.now() - t0

print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())

# Vector and Matrices (preferenciar array)
a = np.matrix([[1, 2], [3, 4]])
a[0, 1]
a.T  # Transposição
a = np.array(a)

# Generating Matrix to work
z = np.zeros(10)
z = np.zeros([10, 10])
o = np.ones(10)
o = np.ones([10, 100])
r = np.random.random([10, 10])
gaussian = np.random.randn(3, 3)
gaussian.mean()
gaussian.var()

# Matrix Products
a = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(a)
inv.dot(a)
a.dot(inv)
np.linalg.det(a)
np.diag(a)
np.diag([1, 2])
a = np.array([1, 2])
b = np.array([3, 4])
np.outer(a, b)
np.inner(a, b)
x = np.random.randn(100, 3)
cov = np.cov(x)
cov.shape
cov = np.cov(x.T)
cov.shape
np.linalg.eigh(cov)
np.linalg.eig(cov)

# Solving Linear System
a = np.array([[1, 2], [3, 4]])
b = np.array([0, 12])
x = np.linalg.inv(a).dot(b)
x = np.linalg.solve(a, b)  # Jeito mais rápido

# Exercicio
a = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
np.linalg.solve(a, b)
