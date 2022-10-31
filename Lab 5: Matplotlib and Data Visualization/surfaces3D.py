# type: ignore
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure(figsize=(15, 10), dpi=80)
# hyperbolic paraboloid
Hyperbolic = fig.add_subplot(2, 4, 1, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b = 0.5, 1
Z = X*X/a - Y*Y/b
Hyperbolic.contour3D(X, Y, Z, 50)
Hyperbolic.set_title('Hyperbolic Paraboloid')

# ellipsoid paraboloid
Elliptic = fig.add_subplot(2, 4, 2, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)
a, b = 0.5, 1
Z = X*X/a + Y*Y/b
Elliptic.contour3D(X, Y, Z, 50)
Elliptic.set_title('Elliptic Paraboloid')

# hyperbolic hyperboloids
# source: Plotting A Hyperboloid StackOverFlow
Hyperbolic_Hyperboloid = fig.add_subplot(2, 4, 3, projection='3d')
r = 1
u = np.linspace(-2, 2, 200)
v = np.linspace(0, 2*np.pi, 60)
[u, v] = np.meshgrid(u, v)

a = 1
b = 1
c = 1
x = a*np.cosh(u)*np.cos(v)
y = b*np.cosh(u)*np.sin(v)
z = c*np.sinh(u)
Hyperbolic_Hyperboloid.contour3D(x, y, z, 50)
Hyperbolic_Hyperboloid.set_title('Hyperbolic Hyperboloid')

# elliptic hyperboloid
# source: Plotting A 3D Hyperboloid StackOverFlow
Elliptic_Hyperboloid = fig.add_subplot(2, 4, 4, projection='3d')
X = np.linspace(-5, 5, 30)
Y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(X, Y)

Z = np.sqrt(0.3*(X ** 2 + Y ** 2) + 1)

Elliptic_Hyperboloid.contour3D(X, Y, Z, 50)
Elliptic_Hyperboloid.contour3D(X, Y, -Z, 50)
Elliptic_Hyperboloid.set_title('Elliptic Hyperboloid')

# sphere
# source: Plotting a 3d cube, a sphere and a vector in Matplotlib StackOverFlow
Sphere = fig.add_subplot(2, 4, 5, projection='3d')
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
Sphere.contour3D(x, y, z, 50)
Sphere.set_title('Sphere')

# cone
# source: 3D plot of the CONE using matplotlib StackOverFlow

Cone = fig.add_subplot(2, 4, 6, projection='3d')
u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:80j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.sqrt(x ** 2 + y ** 2)
Cone.contour3D(x, y, -z, 50)
Cone.set_title('Cone')

# square pyramid
# source: Python 3d Pyramid StackOverFlow
pyramid = fig.add_subplot(2, 4, 7, projection='3d')

v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])
pyramid.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = np.array([[-1, -1, -1], [1, -1, -1],
                 [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])

# plot sides
pyramid.plot_trisurf(verts[:, 0], verts[:, 1],
                     verts[:, 2], alpha=0.5, linewidth=0.2, antialiased=True, color='lightblue')


pyramid.set_title('Square Pyramid')

# parallelepiped
# source: python draw parallelepiped StackOverFlow
parallelepiped = fig.add_subplot(2, 4, 8, projection='3d')
points = np.array([[-1, -1, -1],
                  [1, -1, -1],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1],
                  [1, 1, 1],
                  [-1, 1, 1]])

P = [[2.06498904e-01, -6.30755443e-07,  1.07477548e-03],
     [1.61535574e-06,  1.18897198e-01,  7.85307721e-06],
     [7.08353661e-02,  4.48415767e-06,  2.05395893e-01]]

Z = np.zeros((8, 3))
for i in range(8):
    Z[i, :] = np.dot(points[i, :], P)
Z = 10.0*Z
r = [-1, 1]

X, Y = np.meshgrid(r, r)
parallelepiped.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2], alpha=0.5,
                         linewidth=0.2, antialiased=True)

for i in range(8):
    parallelepiped.text(Z[i, 0], Z[i, 1], Z[i, 2], str(i))

sides = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
         [2, 3, 7, 6], [1, 2, 6, 5], [0, 3, 7, 4]]

for side in sides:
    parallelepiped.plot_trisurf(
        Z[side, 0], Z[side, 1], Z[side, 2], alpha=0.5, linewidth=0.2, antialiased=True, color='lightblue')

parallelepiped.set_title('Parallelepiped')

plt.show()
