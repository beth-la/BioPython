# RCSB - PDB

Protein data bank es una base de datos de proteínas que almacena la conformación y estructura proteicas, 

Archivos PDB: contienen metadatos 

- Header 
- Title 
- Compond 
- Source 
- Keywds 
- Expdata 

Configuración tridimensional de la proteína. 

```R
obj_struc = parser.get_structure("nombre", "archivo.pdb")
# Nos da la llave del modelo 
struc.child_dic
struc.header["structure_method"]

# Para hacer estructuras a partir de un archivo .pdb
from Bio import PDB 
parser = PDB.PDBParser(QUIET=true)
# Crear objeto
struc = parser.get_structure("prot_1fat", "./files/1fat.gdp")
# Pedir llaves al diccionario
struc.child_dic
# Acceder a metadatos 
struc.header.keys()
struc.header["structure_method"]
```

