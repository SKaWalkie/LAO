# Q2: NumPy one-liner
import numpy as np
A = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]], float)
b = np.array([8,-11,-3], float)
x = np.linalg.solve(A,b)
print("x=", x)
