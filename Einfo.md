# Einfo 

```
from Bio import Entrez
from pprint import pprint 

Entrez.email = email 
handle = Entrez.einfo()

# Informacion sin parsear 
result = handle.read()

# Diccionario con bases de datos 
record = Entrez.read(handle)


handle = Entrez.einfo(db= 'Pubmed')
record = Entrez.read(handle)

# Lista de 
record['DbInfo']['FieldList']
```

# Esearch 

```
handle = Entrez.esearch(db="pubmed", term = "biopython")
record = Entrez.read(handle)
# Contar cuantos resultados obtenemos
record["Count"]
handle.close()

# Ids 
record["IdList"]
```

