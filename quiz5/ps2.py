import numpy as np
from numpy.linalg import solve

a = np.array([[3,4], [9,11]])
b = np.array([-250,-250])
x = np.linalg.solve(a, b)
print x