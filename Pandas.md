# Pandas 

Las series son de una dimensión y los data frames de dos.

Series:

- Agregar indices 
- Agregar nombres 

```python

Import pandas as pd
ecoli = pd.series([0.1,0.15,0.19], name = "Matraz", index = ["t1","t2","t2","t4"])

# acceder a valores 
matraz.values 

# las operaciones entre dos series se hacen de acuerdo a los indices 
```

