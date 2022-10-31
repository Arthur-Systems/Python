# type: ignore # ignore
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # in this code it is not required

ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z * 0.5
y = z * 0.5
ax.plot3D(x, y, z, 'green', label='Line')

z = np.linspace(0, 1, 100)
x = np.linspace(1, 1, 100) - z * 0.5
y = np.linspace(1, 1, 100) - z * 0.5
ax.plot3D(x, y, z, 'green', label='Line')

z = np.linspace(0, 1, 100)
x = np.linspace(0, 0, 100) + z * 0.5
y = np.linspace(1, 1, 100) - z * 0.5
ax.plot3D(x, y, z, 'green', label='Line')

z = np.linspace(0, 1, 100)
x = np.linspace(1, 1, 100) - z * 0.5
y = np.linspace(0, 0, 100) + z * 0.5
ax.plot3D(x, y, z, 'green', label='Line')

z = 0
x = np.linspace(0, 1, 100)
y = np.linspace(1, 1, 100)
ax.plot3D(x, y, z, 'green', label='Line')

z = 0
x = np.linspace(1, 1, 100)
y = np.linspace(0, 1, 100)
ax.plot3D(x, y, z, 'green', label='Line')

z = 0
x = np.linspace(0, 1, 100)
y = np.linspace(0, 0, 100)
ax.plot3D(x, y, z, 'green', label='Line')

z = 0
x = np.linspace(0, 0, 100)
y = np.linspace(0, 1, 100)
ax.plot3D(x, y, z, 'green', label='Line')  # plot the curve


ax.set_title('Pyramid')
plt.show(block=True)
