# Q1: Matrix basics (add/sub/mul/transpose/det/rank/inv)
import numpy as np

A = np.array([[2,3,4],[1,0,2],[3,1,1]], float)
B = np.array([[1,2,3],[2,1,0],[1,0,2]], float)

print("A+B=\n", A+B)
print("A-B=\n", A-B)
print("A*B=\n", A@B)
print("A^T=\n", A.T)
print("det(A)=", np.linalg.det(A))
print("rank(A)=", np.linalg.matrix_rank(A))

if abs(np.linalg.det(A)) > 1e-9:
    print("A^{-1}=\n", np.linalg.inv(A))
else:
    print("A has no inverse (det=0)")

# ---- OPTIONAL QUESTIONS BELOW ----
# Remove # from the lines you need (no indent needed)

# eigvals, eigvecs = np.linalg.eig(A)
# print("Eigenvalues:", eigvals)
# print("Eigenvectors:\n", eigvecs)

# print("A*B == B*A ?", np.allclose(A@B, B@A))

# M = A
# print("Orthogonal?", np.allclose(M.T@M, np.eye(M.shape[0])))

# b = np.array([14,31,50], float)
# Aug = np.c_[A, b]
# print("rank([A|b]) =", np.linalg.matrix_rank(Aug))

# x = np.linalg.solve(A, b)
# print("Verify A@x == b ?", np.allclose(A@x, b))
