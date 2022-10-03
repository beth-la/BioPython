'''
Name 
    Qscore umbral 
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    
Category
    Python .\src\qscore_umbral.py -f .\data\sample.fastq -o results/qscore_result.fasta -u 25
    
Usage
    qscore_umbral.py [-h] -f path/to/file -o path/to/file -u UMBRAL 
    
Arguments
    -h --help
    -f path/to/file --FASTQ
    -u --UMBRAL
See also
    None
'''
from Bio import SeqIO
from numpy import mean
import argparse

# Agregar paso de argumentos

arg_parser = argparse.ArgumentParser(description="Evaluar Qscore en relacion a un umbral dado")
arg_parser.add_argument("-f", "--FASTQ",
                    metavar="path/to/file",
                    help="Archivo en formato Fastq",
                    required=True)

arg_parser.add_argument("-o", "--OUTPUT",
                    metavar="path/to/file",
                    help="Ruta de archivo de salida",
                    required=True)

arg_parser.add_argument("-u", "--UMBRAL",
                    type= int,
                    help="Valor de umbral minimo esperado",
                    required=True)

arguments = arg_parser.parse_args()

def seq_umbral(umbral):
    '''
    Elimina las secuencias si alguna de las bases se encuentra por debajo del umbral 
    para el valor de su Qscore.
    Parameters:
        umbral (int): Valor del umbral deseado. 
    Returns:
        message (str): Mensaje que indica que el archivo esta listo. 
    '''
    with open(arguments.OUTPUT, "w") as file:
        n=0
        for record in (SeqIO.parse(arguments.FASTQ, "fastq")):
            # Si el valor de qscore minimo esta por debajo del umbral entonces esta no se 
            # tomara en cuenta
            if min(record.letter_annotations['phred_quality']) >= umbral:
                file.write(f"{record.id}\n{record.seq}\n")
                n += 1
    return(f"File ready: {arguments.OUTPUT}, number of readings: {n}")

# Llamamos a la funcion
result=seq_umbral(arguments.UMBRAL)
print(result)