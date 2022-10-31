import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))     # the data type of the object arr
print(arr.dtype)

for i in dir(arr):
    print(i)
print(arr.size)
print(arr.sum())
print(arr.shape)

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3D)

print(arr.ndim)
print(arr2D.ndim)
print(arr3D.ndim)
arr5D = np.array([1, 2, 3, 4], ndmin=5)
print(arr5D)
print(arr5D.ndim)

for k in np.nditer(arr3D):
    print(k)

filter_ = [True, False, True, False, True]
print(arr[filter_])

print(arr[arr > 2])

print(arr[arr % 2 == 0])

X = np.arange(1, 11)
print(X)

Y = np.log(X)
print(Y)

Z = np.sin(X)
print(Z)

X2 = np.rad2deg(X)
print(X2 % 360)


nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2])
