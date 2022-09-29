# Biopython

```python
# format inserta información en un string, en donde se le señale con llaves.
print("Codon de inicio en las posiciones {}".frotmat(posicion[1:]))
```

## Objetos SeqRecord 

SeqIO.Parse genera objetos Bio.SeqRecord 

Atributos principales 

- ID: identificador (cadena) objeto.id
- Seq: secuencia (objeto Seq o similar) objeto.seq

Atributos adicionales 

- name: nombre de la secuencia, como el nombre del gen (str)
- description: texto adicional
- dbxrefs: lista de referencias cruzadas de bases de datos (listas de cadenas) 
- features: cuaquier sub features definidos
- anonation

SeqIO.parse(): toma un archivo y su respectivo formato para regresar un iterador de SeqRecord

```python
# Utilizar SeqIO
from Bio import SeqIO
for record in SeqIo.parse('archivo.fasta','fasta'):
	Print(record)
	
with open('archivo.fasta') as handle:
	for record in SeqIO.parse(handle,'fasta')
		print(record)

# Imprimir bonito
pprint.pprint(proyect)

# SeqIO.to_dict
id_dict = SeqIO.to_dict(SeqIO.pase("archivo.fasta","fasta"))

from Bio import SeqIO
import Bio
for record in SeqIO.parse('data/fasta.fasta','fasta'):
    print(f"ID {record.id}")
    print(f"len {len(record)}")
    print(f"Traduccion {record.seq.translate(to_stop=True)}")
```

Con listas:

```python
from Bio import SeqIO
id_list = list(SeqIO.parse("files/clase_2/seq.nt.fa", "fasta"))
# Imprimir ID
print(id_list[-1].id, '\n') 

# Hacer un fasta con ciertas secuencias 
with open("files/clase_2/filtered.fasta", "w") as out_handle:
    for record in SeqIO.parse('archivos_trabajo/seq.nt.fa', "fasta"):
        if record.id in seq_ids:
            SeqIO.write(record, out_handle, "fasta")
```

Subset:

```python
seq_ids =[ids]

with open(archivo) as archivo
for record in SeqIO.parse(filepath, "fasta"):
	if record in seq_ids:
		SeqIO.write(record, archivo, "fasta")
```

Score de calidad

El qScore es de 3 significa que P=0.5, por lo que hay 50% de probabilidad de que la base esté mal. 

# Para archivos FASTQ

```python
for record in SeqIO.parse("arhivo", "fastq"):
	print(f"{record.id}{record.seq}")
	# Imprimir el Q score
	print(record.letter_annotations["phared_quality"])
	print(record.letter.annotation.keys())
```

