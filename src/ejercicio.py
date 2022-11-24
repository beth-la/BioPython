import numpy as np

array_gml = np.genfromtxt("docs/prod_gml.csv", delimiter= ",")

array_gL= array_gml * 1000
#print(f"En unidades g/l{array_gL}")

idx_cost = np.genfromtxt("docs/ind_cost.csv", delimiter= ",")
cost_30 = idx_cost * 1.75
cost_35 = idx_cost * 0.8
#print(f"Costo a 30: {cost_30} Csoto a 35: {cost_35}")

costo = idx_cost * 1.5 / array_gL[]
print(cost_30)