import matplotlib.pyplot as plt
import numpy as np

# Chart
x = np.linspace(0, 10, 10)
y = np.sin(x)
plt.xlabel('Time')
plt.ylabel('Function time')
plt.title('Chart')
plt.plot(x, y)
plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# Scatter
import pandas as pd
df = pd.read_csv('data_1d.csv', header=None).as_matrix()
x = df[:, 0]
y = df[:, 1]
plt.scatter(x, y)
plt.show()

# Plot and Scatter
x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()

# Histogram
plt.hist(x)
plt.show()

r = np.random.random(10000)
plt.hist(r)
plt.show()

plt.hist(r, bins=20)
plt.show()

y_res = y_line - y
plt.hist(y_res)
plt.show()

# Plotting images
df = pd.read_csv('train.csv')
df.shape
df = df.as_matrix()
im = df[0, 1:]
im.shape
im = im.reshape(28, 28)
plt.imshow(im)
plt.imshow(im, cmap='gray')
plt.show()
plt.imshow(255-im, cmap='gray')
plt.show()
