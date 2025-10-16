# Q3: PuLP (Max/Min; ≤ or ≥ by typing <= or >=)
import pulp as pl

sense = "max"  # or "min"
m = pl.LpProblem("LPP", pl.LpMaximize if sense=="max" else pl.LpMinimize)

x = pl.LpVariable('x', lowBound=0)
y = pl.LpVariable('y', lowBound=0)
z = pl.LpVariable('z', lowBound=0)

m += 5*x + 4*y + 6*z
m += 2*x + 1*y + 1*z <= 10
m += 1*x + 3*y + 2*z <= 12
# for ≥ just write >= ; for 2-var drop z terms

m.solve()
print("Z=", pl.value(m.objective))
print("x,y,z=", x.value(), y.value(), z.value())
