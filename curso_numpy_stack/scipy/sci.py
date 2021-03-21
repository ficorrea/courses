from scipy.stats import norm
norm.pdf(0)
norm.pdf(0, loc=5, scale=10)

# PDF and CDF
import numpy as np
r = np.random.random(10)
norm.logpdf(r)
norm.cdf(r)

# Gaussian 1-D
import matplotlib.pyplot as plt
r = np.random.randn(10000)
plt.hist(r, bins=100)
plt.show()

r = 10*np.random.randn(10000) + 5
plt.hist(r, bins=100)
plt.show()

# Gaussian spherical
r = np.random.randn(10000, 2)
plt.scatter(r[:, 0], r[:, 1])
plt.show()

r[:, 1] = 5*r[:, 1] + 2
plt.scatter(r[:, 0], r[:, 1])
plt.show()

plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

# General Multivariate Normal
from scipy.stats import multivariate_normal as mvn
cov = np.array([[1, 0.8], [0.8, 3]])
mu = np.array([0, 2])
r = mvn.rvs(mean=mu, cov=cov, size=1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

r = np.random.multivariate_normal(mean=mu, cov=cov, size=1000)
plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()

# Other functions
x = np.linspace(0, 100, 10000)
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)
plt.plot(y)
plt.show()

Y = np.fft.fft(y)
plt.plot(abs(Y))
plt.show()


