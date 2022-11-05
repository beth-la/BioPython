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
from calendar import c
from contextlib import suppress
from ctypes.wintypes import HANDLE
from dataclasses import field
from Bio import Entrez
from pprint import pprint
import argparse
import re
from Bio import SeqIO
Entrez.email = 'blopez.lcg.unam.mx'

path = "results/entrez_ids"

with open(path, "r") as archivo:
    information = archivo.read()

my_list = information.split(">")
my_list = [element.split("\n") for element in my_list]
my_list.pop(0)
none = [element.pop(-1) for element in my_list]

list_article = []
with open("results/out_efetch", "w") as archivo:
    for organism in my_list:
    #print(organism)
        for db in organism[1:]:
            db_name_id = db.replace(" ",",").split(":")
            if db_name_id[0] == "pubmed" or db_name_id[0] == "pmc":
                handle = Entrez.efetch(db= db_name_id[0], id=db_name_id[1], rettype="fasta", retmode="text")
                read_myhandle = handle.read()
                list_article.append(read_myhandle)
                #archivo.write(f"{read_myhandle}\n")

print(list_article[0])