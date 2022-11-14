import matplotlib.pyplot as plt    # need for plotting an image
import matplotlib.image as mpimg   # need for image loading and saving
import numpy as np                 # need for manipulating arrays
from numpy import linalg as la     # need for finding SVD

# you need to download the image from Canvas/Files/Labs
img = mpimg.imread('redbox.jpg')
# plt.imshow(img)
# plt.show()
print(img.ndim)
X, Y, Z = img.shape                # get the image array dimensions
print(X, Y, Z)
print(img.dtype)                   # array value type
print(img.max())                   # max number in the array
print(img.min())                   # min number in the array

# # red pixels
# red = img[:, :, 0]
# print('red pixels:')
# print(red)

# # green pixels
# green = img[:, :, 1]
# print('green pixels:')
# print(green)

# # blue pixels
# blue = img[:, :, 2]
# print('blue pixels:')
# print(blue)


AllPixes = np.asarray(img)
print(AllPixes)
print(AllPixes.shape)

# # find SVD
# U, s, Vt = la.svd(red)
# print(U.shape, s.shape, Vt.shape)

# # verify SVD
# Sigma = np.zeros((X, Y))  # convert s (a 1D array) into Sigma (a 2D-array)
# for i in range(X):
#     Sigma[i, i] = s[i]

# # verify the equality of the original array and decomposed array
# print(np.allclose(red, U @ Sigma @ Vt))

# # visualize the diagonal values of SVD
# plt.plot(s)
# plt.show()

# # choose significant values in the diagonal of SVD
# k = 50
# red_approx = U @ Sigma[:, :k] @ Vt[:k, :]
# print(red_approx.shape)
# plt.imshow(red_approx, cmap="Reds")
# plt.show()

# # choose significant values in the diagonal of SVD
# k = 50
# blue_approx = U @ Sigma[:, :k] @ Vt[:k, :]
# print(blue_approx.shape)
# plt.imshow(blue_approx, cmap="Blues")
# plt.show()

# # choose significant values in the diagonal of SVD
# k = 50
# green_approx = U @ Sigma[:, :k] @ Vt[:k, :]
# print(blue_approx.shape)
# plt.imshow(green_approx, cmap="Greens")
# plt.show()

# img_recon = np.stack((red, green, blue), axis=2)
# plt.imshow(img_recon)
# plt.show()

# # apply SVD to all pixels at once
# img_transposed = np.transpose(img, (2, 0, 1))
# U, s, Vt = la.svd(img_transposed)
# print(U.shape, s.shape, Vt.shape)

# Sigma = np.zeros((Z, X, Y))
# for j in range(3):
#     np.fill_diagonal(Sigma[j, :, :], s[j, :])

# k = 50
# img_approx = U @ Sigma[..., :k] @ Vt[..., :k, :]
# img_approx = np.transpose(img_approx, (1, 2, 0))
# img_approx = img_approx - img_approx.min()
# img_approx = img_approx / img_approx.max()
# plt.imshow(img_approx)
# plt.show()

# plt.imsave("octopus_new.jpg", img_approx)
