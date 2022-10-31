from matplotlib import pyplot as plt
import numpy as np
import math
# make an array of values from 0.0 to 2π with a step 0.05
x = np.arange(0, math.pi*2, 0.05)
# make an array of values using the function sin(x)
print(x, np.size(np.sin(x)))
