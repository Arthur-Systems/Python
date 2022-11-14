import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def cylinder(radius, height):
    theta = np.linspace(0, 2*np.pi, 100)
    zplot = np.linspace(0, height, 100)
    theta, z = np.meshgrid(theta, zplot)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.contour3D(x, y, z, 50)
    plt.show()


if __name__ == "__main__":

    cylinder(1, 2)
    cylinder(2, 10)
