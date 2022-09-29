# Ejercicio 
from Bio import SeqIO
from numpy import mean

import argparse

# Agregar paso de argumentos

arg_parser = argparse.ArgumentParser(description="Calcula el porcentaje de nucleotidos: AT y CG")

arg_parser.add_argument("-f", "--FASTQ",
                    metavar="path/to/file",
                    help="File with ADN sequences",
                    required=True)

arg_parser.add_argument("-o", "--OUTPUT",
                    metavar="path/to/file",
                    help="File with ADN sequences",
                    required=False)

arg_parser.add_argument("-u", "--UMBRAL",
                    type= int,
                    help="File with ADN sequences",
                    required=True)

arguments = arg_parser.parse_args()

def seq_umbral(umbral):
    with open(arguments.OUTPUT, "w") as file:
        n=0
        for record in (SeqIO.parse(arguments.FASTQ, "fastq")):
            if min(record.letter_annotations['phred_quality']) >= umbral:
                file.write(f"{record.id}\n{record.seq}\n")
                n += 1
    return(f"File ready: {arguments.OUTPUT}, lecture number = {n}")

result=seq_umbral(arguments.UMBRAL)
print(result)

