# Q2: Gauss–Seidel (simple)
import numpy as np
A = np.array([[4,1,2],[1,5,1],[2,1,6]], float)
b = np.array([4,7,9], float)
x = np.zeros_like(b)
for _ in range(200):
    x_old = x.copy()
    for i in range(len(b)):
        s = A[i,:i]@x[:i] + A[i,i+1:]@x[i+1:]
        x[i] = (b[i]-s)/A[i,i]
    if np.allclose(x,x_old,atol=1e-8): break
print("x≈", x)
