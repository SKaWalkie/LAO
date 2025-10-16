# Q3: SciPy linprog (Max/Min; ≤ and ≥)
from scipy.optimize import linprog
import numpy as np

sense = "max"                  # "max" or "min"
c  = np.array([5,4,6], float)  # Z = 5x + 4y + 6z

# Put ≤ constraints here
A_le = np.array([[2,1,1],[1,3,2]], float)
b_le = np.array([10,12], float)

# Put ≥ constraints here (as written); leave empty if none
A_ge = np.empty((0,3)); b_ge = np.empty(0)

# Convert ≥ to ≤ and solve
A_ub = A_le.copy(); b_ub = b_le.copy()
if A_ge.size: A_ub = np.vstack([A_ub,-A_ge]); b_ub = np.concatenate([b_ub,-b_ge])

c_eff = -c if sense=="max" else c
res = linprog(c_eff, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None)]*len(c), method="highs")

print(("Max Z","Min Z")[sense=="min"], (-res.fun if sense=="max" else res.fun))
print("x*=", res.x)
