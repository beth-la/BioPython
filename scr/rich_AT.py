''' Name 
    search AT rich regions
    
Version
    1.0
    
Author 
    Lopez A. Brenda.
    
Descripcion
    Programa que busca regiones ricas en AT
    
Category
    DNA sequence
    
Usage
    Python rich_at.py -f path/to/file [-n ] 
        
Arguments
    -h --help
    -f --file 
    -r --region
    
See also
    None
    
'''

import argparse
import re 

arg_parser = argparse.ArgumentParser(description="Search AT rich regions")
arg_parser.add_argument("-f", "--file",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ADN",
                    required=True)
         
arg_parser.add_argument("-r", "--region",
                    help="Tamaño minimo a buscar AT",
                    type=int,
                    required=False)

args = arg_parser.parse_args()

with open(args.file, "r") as seq_file:
    dna = seq_file.read()
    
def evaluate(dna):
    if(re.search("[^ATGC]+", dna)):
        return(0)
    else:
        return(1)

prueba = evaluate(dna)
print(prueba)