# Q2: Cramer's rule (tiny)
import numpy as np
A = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]], float)
b = np.array([8,-11,-3], float)
d = np.linalg.det(A)
if abs(d)<1e-9: print("no unique solution")
else:
    x = []
    for k in range(A.shape[1]):
        Ak = A.copy(); Ak[:,k] = b
        x.append(np.linalg.det(Ak)/d)
    print("x=", x)
