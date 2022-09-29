# BioPython 

**Nunpy** 

Numerical Python 

- Computo orientado a arrays 
- Arrays multidimensionales 
- Vectorización y Broadcasting

**Pandas**

Objetos Dataframes rapidos para manipular.

**Matplotlib** 

Emplea pyplot

Conecta NunPy y Pandas 

Exploración de análisis de datos y plots para publicaciones. 

## Manejo de secuencias 

importar modulos.

```python
# Un objeto secuencia  no mutable
from Bio.Seq import Seq 
secuencia = seq("AAAAAAAA")

# Un objeto secuencia mutable 
from Bio.Seq import MutableSeq 
mutableSeq = MutableSeq("AAAA")

```

```python
#Inverso de una cadena. 
#Con un objeto seq.
from Bio.Seq import Seq
secuencia = Seq('AAATTTGCA')
secuencia.complement()
secuencia.reverse_complement()

#Traduccion 
secuencia.translate(to_stop=True)

#Transcrito 
secuencia.transcribe()

#Retrotranscrito 
secuencia.back_transcribe()

```

```python
# Como un objeto de lista 
secuencia[3:5]
```

```python
import re 
codones = re.findall(r'(.{3}))', str(seqonj))

```

```python
# SeqUtils
from Bio import SeqUtils 

patron = seq('ACG')
secuencia = seq('AACGCGATC')

RESULTS = SeqUtils.nt_search(str(sequence), pattern)
print(RESULTS)
```

```
secuencia_ com = secuencia.reverse_complement()

pattern = 'GCG'
results = SeqUtils.nt_search(str(secuencia_com), pattern)
```

