'''
Name 
    Dif orfs DNA
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que procesa un archivo fasta, busca los posibles orfs y genera un nuevo archivo
    con las lecturas desde los diferentes orfs.
    
Category
    Fasta
    
Usage

    
Arguments
    -h --help
       
See also
    None
'''
from aminoacids_module import codon_format
from Bio import SeqUtils
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Seq
import argparse
import Bio 

arg_parser = argparse.ArgumentParser(description="Obtener secuencia proteica con mas larga")
                    
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo en formato fasta con las secuencias",
                    required=True)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Ruta para el archivo de salida",
                    required=True)

arguments = arg_parser.parse_args() 

def seq_orfs(input_path, output_path):
    '''
    Toma un archivo en formato fasta y genera un archivo con sus secuencias a partir de sus orfs. 
    Parameters:
        input_path (str): Archivo fasta que cotiene las secuencias.
        output_path (str): Archivo que contiene el 
    Returns:
        
    '''
    id_dictionary = SeqIO.to_dict(SeqIO.parse(input_path,"fasta"))
    list_DNA_orfs = []
    with open(output_path,"w") as archivo:
        for keys in id_dictionary:
            orf = Seq('ATG')
            find = SeqUtils.nt_search(str(id_dictionary[keys].seq),orf)
            orf_num = 0
            for position in find[1:]:
                orf_num += 1
                orf_sequence = codon_format(str(id_dictionary[keys].seq[position:]))
                archivo.write(f">{keys} orf number: {orf_num}\n")
                archivo.write(f"{' '.join(orf_sequence)}\n")
    return(1)

seq_orfs(arguments.FILE, arguments.OUTPUT)
print("File created")  