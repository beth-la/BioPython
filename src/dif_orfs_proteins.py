'''
Name 
    Dif orfs proteins
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que procesa una cadena de ADN, busca los posibles orfs y regresa la cadena proteica mas larga
    generada.
    
Category
    Aminoacid sequence
    
Usage
    Python dif_orfs_proteins.py [-h] [-s SEQUENCE] [-f path/to/file] [-o OUTPUT] [-p]
    Python .\src\dif_orfs_proteins.py -f .\data\sequence.txt -p -o '.\data\output_peptid.txt'
    
Arguments

    -h --help
    -s --sequence
    
See also
    None
'''

# Importando librerias
# Importando aminoacids_module
# Asignando los argumentos que recibe el programa

from xmlrpc.client import ProtocolError
from Bio import Seq 
from Bio.Seq import Seq 
from Bio import SeqUtils
import argparse
import warnings

arg_parser = argparse.ArgumentParser(description="Obtener secuencia proteica con mas larga")
arg_parser.add_argument("-s", "--SEQUENCE",
                    help="secuencia de ADN a procesar",
                    type = Seq,
                    required=False)
                    
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo con secuencia de ADN",
                    required=False)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Ruta para el archivo de salida",
                    required=False)

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla la secuencia peptidica",
                    action = 'store_true',
                    required= False)
                    
arguments = arg_parser.parse_args() 

def max_prot_orfs(ADN):
    '''
    Toma una secuencia de ADN y la traduce a su producto proteico a partir de los orfs encontrados, regresa 
    el peptido con mayor cantidad de aminoacidos. 
    Parameters:
        ADN (str): Secuencia de aminoacidos
    Returns:
        max(proteins) (seq): Secuencia peptidica con mayor cantidad de aminoacidos 
    '''
    orf = Seq('ATG')
    find = SeqUtils.nt_search(str(ADN),orf)
    if len(find) == 1:
        return(f"No se encontraron orfs: {orf} en la secuencia")
    else:
        proteins = [ADN[position:].translate(to_stop = True) for position in find[1:]]
        return(max(proteins))

# Ignorando warnings de Biopython:
# BiopythonWarning: Partial codon, len(sequence) not a multiple of three. Esplicitly trim the sequence or add 
# triling N before translation. This may become an error in future. 

warnings.filterwarnings('ignore')
warnings.warn('BiopythonWarning')

# Si el usurio ingresa la secuencia por teclado
if arguments.SEQUENCE:
    proteinas = max_prot_orfs(arguments.SEQUENCE)

# Si la secuencia se encuentra en un archivo 
if arguments.FILE:
    with open(arguments.FILE, 'r') as archivo:
        ADN = archivo.read().replace('\n','')
    proteinas = max_prot_orfs(Seq(ADN))

# Si se requiere imprimir el resultado a pantalla
if arguments.PRINT:
    print(f"La secuencia proteica con mayor contenido de aminoacidos es: {proteinas}")

# Si se quiere pasar el resultado a un archivo
if arguments.OUTPUT:
    with open(arguments.OUTPUT,'w') as archivo:
        archivo.write(f"La secuencia proteica con mayor contenido de aminoacidos es:\n{proteinas}")   