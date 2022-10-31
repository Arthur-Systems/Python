import numpy as np
import matplotlib.pyplot as plt

maxiter = 20
h, w = 400, 400
y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
c = x+y*1j
z = c
divtime = maxiter + np.zeros(z.shape, dtype=int)

for i in range(maxiter):
    z = z**2 + c
    diverge = z*np.conj(z) > 2**2
    div_now = diverge & (divtime == maxiter)
    divtime[div_now] = i
    z[diverge] = 2

img = divtime
rotated = np.rot90(img)  # rotate the image
plt.imshow(rotated, cmap='hot')
plt.xlim(0, w - 150)  # crop the image
plt.ylim(0, h - 150)
plt.imsave("mandelbrot.jpeg", img)
plt.show()
