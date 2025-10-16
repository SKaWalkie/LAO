# Q2: Gauss elimination (short)
import numpy as np
A = np.array([[3,-2,1],[-2,1,4],[1,4,-5]], float)
b = np.array([13,11,-31], float)
M = np.c_[A,b].astype(float); n = M.shape[0]
for k in range(n-1):
    for i in range(k+1,n):
        M[i,k:] -= (M[i,k]/M[k,k]) * M[k,k:]
x = np.zeros(n)
for i in range(n-1,-1,-1):
    x[i] = (M[i,-1] - M[i,i+1:]@x[i+1:]) / M[i,i]
print("x=", x)
