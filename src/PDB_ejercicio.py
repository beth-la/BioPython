# Obteniendo informacion del archivo. 
from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1kcw", "data/1kcw.pdb")
#print(f"Structure method:\n\t{struc.header['structure_method']}\n")
#print(f"Resolution:\n\t{struc.header['resolution']}\n")

# Haciendo un modelo
model = struc[0]
cadenas = model.child_list[0]
model.id = "Modelo PDB"

#cisteinas = [[residuo.resname, residuo.get_id()[1]] for residuo in cadenas if residuo.get_resname() == "CYS"]
cisteinas = [[residuo.resname, residuo.get_id()[1]] for residuo in cadenas if residuo.get_resname() == "CYS"]