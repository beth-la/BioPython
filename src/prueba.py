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
    Python dif_orfs_dna.py -f data/fasta_file.fasta -o results/out.fasta
    Python dif_orfs_dna.py [-h] -f path/to/file -o OUTPUT
    
Arguments
    -h --help
    -f --FILE path/to/file
    -o --OUTPUT
    
See also
    None
'''
from aminoacids_module import codon_format
from Bio import SeqUtils
from Bio.Seq import Seq
from Bio import SeqIO
from ADN_module import complement_adn
import argparse
import Bio 

arg_parser = argparse.ArgumentParser(description="Obtener archivo fasta")
                    
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
    Toma un archivo en formato fasta y genera un nuevo archivo fasta con cada una de 
    las secuencias posibles a partir de los ORFs encontrados. 
    Parameters:
        input_path (str): Dirreccion del archivo fasta de entrada 
        output_path (str): Direccion que se desea para el archivo de salida 
    Returns:
        1 (int)
    '''
    id_dictionary = SeqIO.to_dict(SeqIO.parse(input_path,"fasta"))
    list_DNA_orfs = []
    with open(output_path,"w") as archivo:
        for keys in id_dictionary:
            orf = Seq('ATG')
            find = SeqUtils.nt_search(str(id_dictionary[keys].seq),orf)
            orf_num = 0
            if len(find) == 1:
                return(f"No se encontraron orfs: {orf} en la secuencia")
            # Se toman los valores de la lista generada con nt_search a exepcion del elemento 0
            # Se corta la secuencia a partir de la posicion en donde se encontro un ORF
            # Se llama a la funcion del modulo codon format para que formatee la secuencia generada 
            # a formato de tripletes.
            for position in find[1:]:
                orf_num += 1
                orf_sequence = (str(id_dictionary[keys].seq[position:]))
                for op_frame in range(0,len(orf_sequence)):
                    orf_sequence_complement = (complement_adn(orf_sequence[op_frame:]))
                    if op_frame < 3:
                        archivo.write(f">{keys} orf number: {orf_num} open reading frame: {op_frame+1}\n")
                        archivo.write(f"{' '.join(codon_format(orf_sequence[op_frame:]))}\n")
                        archivo.write(f">{keys} orf number: {orf_num} open reading frame: -{op_frame+1}\n")
                        archivo.write(f"{' '.join(codon_format(orf_sequence_complement))}\n")
    return(1)

# Llamamos a la funcion 
seq_orfs(arguments.FILE, arguments.OUTPUT)
print("File created")  
