'''
Name
    GenBank_search.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion

    
Category
    GenBank 
    
Usage

Arguments
    -h --help
    -f --FILE
    -o --OUTPUT 
    -p --PRINT
    -g --GENES
    
See also
    None
'''
from ctypes.wintypes import HANDLE
from Bio import Entrez
import argparse
import re
from Bio import SeqIO

Entrez.email = 'blopez.lcg.unam.mx'

path = "results/entrez_ids"

handle = Entrez.efetch(db= "pmc", id="9494746", rettype="abstract", retmode="text")
read_myhandle = handle.read()
print(read_myhandle)