import matplotlib.pyplot as plt
import matplotlib


fig = plt.figure(figsize=(15, 10), dpi=80)

s = fig.add_subplot(3, 2, 1, projection='3d')

s = fig.add_subplot(3, 2, 2, projection='3d')
s = fig.add_subplot(3, 2, 3, projection='3d')

plt.show()
