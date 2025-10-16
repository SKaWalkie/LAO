# Q2: Gauss–Jordan (short)
import numpy as np
A = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]], float)
b = np.array([8,-11,-3], float)
M = np.c_[A,b].astype(float); n = M.shape[0]
for i in range(n):
    M[i] /= M[i,i]
    for j in range(n):
        if j!=i: M[j] -= M[j,i]*M[i]
print("x=", M[:,-1])
