'''
Name
    Numpy test
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Ejercicios utilizando herramientas de Numpy 
    
Category
    Numpy
    
Usage
    Python numpy_test.py [-h] 
    
Arguments
    -h --help
    
See also
    None
'''
import numpy as np

# Ejercicio 1 (parte 1):
# Convertir de g/ml a g/L a partir de la informacion encontrada en el archivo  prod_gml.csv
array_gml = np.genfromtxt("docs/prod_gml.csv", delimiter= ",")
array_gL= array_gml * 1000
print(f"Unidades en g/ml:\n{str(array_gml).replace('[',' ').replace(']',' ')}\nUnidades en g/L:\n{str(array_gL).replace('[',' ').replace(']',' ')}\n")

# Ejercicio 2 (parte 2):
# A partir de los costos de los inductores para cada gen, obtener los costos a temperatura a 30 y 35 grados con 1.75 y 0.8 unidades del inductor respectivamente.
idx_cost = np.genfromtxt("docs/ind_cost.csv", delimiter= ",")
cost_30 = idx_cost * 1.75
cost_35 = idx_cost * 0.8
print(f"Costo a 30 grados: {str(cost_30).replace('[',' ').replace(']',' ')}\n")
print(f"Costo a 35 grados: {str(cost_35).replace('[',' ').replace(']',' ')}\n")

# Ejercicio 2:
# Calcular el costo a cada temperatura para la produccion de cada gene en g/L, costo unitario.
cost_30_gl = cost_30 / array_gL[:,0]
cost_35_gl = cost_35 / array_gL[:,1]

# Ejercicio 3:
# Acceder con boleanos a aquellos valores para los cuales es mas barato por unidad a una temperatura de 30 grados 
cheaper_30 = cost_30_gl[(cost_30_gl-cost_35_gl)<0]
position = np.where(cost_30_gl==cheaper_30)
print(f"Para el gene {str(position[0]+1).replace('[','').replace(']','')} el costo a 30 {str(cheaper_30).replace('[','').replace(']','')} es mas barato que el costo a 35 grados:{str(cost_35_gl[position[0]]).replace('[','').replace(']','')}\n")