'''
Name
    GenBank_search.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Obtiene informacion de un archivo de GenBank y busca una lista de genes 
    dada por el usuario para regresar sus primeros 15 nucleotidos de ADN, ARN y 
    su traduccion.
    
Category
    GenBank 
    
Usage
    Python GenBank.py [-h] -f path/to/file -o OUTPUT [-p] -g GENES 
    py .\src\GenBank.py -f data/virus.gb -o results/GenBank_resuls.txt -g N G L -p
Arguments
    -h --help
    -f --FILE
    -o --OUTPUT 
    -p --PRINT
    -g --GENES
    
See also
    None
'''
# Importando librerias 
from Bio import SeqIO
import argparse

arg_parser = argparse.ArgumentParser(description="Obtener informacion de un archivo GenBank")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo en formato GenBank",
                    required=True)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Ruta para el archivo de salida",
                    required=True)

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla los datos obtenidos",
                    action = 'store_true',
                    required= False)
                    
arg_parser.add_argument("-g","--GENES",
                    help = "Lista de genes a buscar",
                    type = str,
                    nargs = '+',
                    required= True)
                    
arguments = arg_parser.parse_args()

# Obteniendo informacion del archivo
def get_info(input, output, genes):
    '''
    Toma un archivo en formato GenBank y extrae informacion de el, devolviendo un archivo.
    Extrae:
        Organismo, fecha, pais, fuente de aislamiento, primeros 15 nucleotidos de ADN y ARN de los 
        genes solicitados por el usuario, posteriormente los traduce y devuelve una secuencia peptidica.
    Parameters:
        input (str): Ruta hacia el archivo de entrada que contiene la informacion en formato GenBank 
        output (str): Ruta en donde se encuentra el archivo que contendra la informacion obtenida
        genes (list): Lista de genes a buscar en el archivo
    Returns:
        0 (int)
    '''
    with open(output,"w") as file:
        # Obtenemos la informacion del archivo.
        for gb_record in SeqIO.parse(input,"genbank"):
            file.write(f"GeneBank file information: {input}\n")
            file.write(f"\tOrganism:\n\t\t{' '.join(gb_record.features[0].qualifiers['organism'])}\n")
            file.write(f"\tDate:\n\t\t{gb_record.annotations['date']}\n")
            file.write(f"\tCountry:\n\t\t{' '.join(gb_record.features[0].qualifiers['country'])}\n")
            file.write(f"\tIsolation source:\n\t\t{' '.join(gb_record.features[0].qualifiers['isolation_source'])}\n")
            # Buscamos cada gen dado por el usuario en el archivo, para asi obtener en donde empieza 
            # y termina su secuencia, posteriormente se transcribe y traduce.
            for gene in genes:
                for features in gb_record.features: 
                    if features.type == "gene" and features.qualifiers["gene"][0] == gene:
                        ADN = gb_record.seq[features.location.nofuzzy_start:features.location.nofuzzy_end]
                        ARN = ADN[:15].transcribe()
                        protein = ADN[:15].translate()
                        file.write(f"\tGene:\n\t\t{gene}\n")
                        file.write(f"\tADN:\n\t\t{ADN[:15]}\n")
                        file.write(f"\tARN:\n\t\t{ARN}\n")
                        file.write(f"\tProtein:\n\t\t{protein}\n")
    return(0)
    
final_file = get_info(arguments.FILE, arguments.OUTPUT, arguments.GENES)
if not arguments.PRINT:
    print(f"File ready, path: {arguments.OUTPUT}")
# Si el usuario quiere imprimir el archivo a pantalla: 
if arguments.PRINT:
    with open (arguments.OUTPUT, "r") as file:
        content = file.read()
    print(content)