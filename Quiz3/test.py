import numpy as np
x = np.arange(0, np.pi*2, 0.1)
y = np.cos(x) + np.sin(x)

# print(np.where(y == np.max(y)[0]))
print(x[np.where(y == max(y))[0][0]])
print(x[np.argmax(y)])

print(
    np.where(y == max(y))[0][0])
print(y[np.argmax(x)])
print(np.argmax(y))
