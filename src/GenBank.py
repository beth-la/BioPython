'''
Name
    GenBank.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Obtiene informacion de un archivo de GenBank:
        Nombre, fecha, organismo, pais y ubicacion.
    
Category
    GenBank 
    
Usage
    Python GenBank.py [-h] -f path/to/file -o OUTPUT [-p]
    py .\src\GenBank.py -f data/virus.gb -o results/GenBank_resuls.txt -p
Arguments
    -h --help
    -f --FILE
    -o --OUTPUT 
    -p --PRINT
    
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
                    help = "Imprimir a pantalla la secuencia peptidica",
                    action = 'store_true',
                    required= False)
                    
arguments = arg_parser.parse_args()

# Obteniendo informacion del archivo
with open(arguments.OUTPUT,"w") as file:
    for gb_record in SeqIO.parse(arguments.FILE,"genbank"):
        file.write("Informacion obtenida del archivo\n")
        file.write(f"Name:\n\t{gb_record.name}\n")
        file.write(f"Date:\n\t{gb_record.annotations['date']}\n")
        file.write("Features:\n")
        file.write(f"\tOrganism: {' '.join(gb_record.features[0].qualifiers['organism'])}\n")
        file.write(f"\tCountry: {' '.join(gb_record.features[0].qualifiers['country'])}\n")
        file.write(f"\tIsolation source: {' '.join(gb_record.features[0].qualifiers['isolation_source'])}\n")
        file.write(f"\tLocation: {gb_record.features[0].location}\n\tType: {gb_record.features[0].type}\n")
        # Si el usuario quiere imprimir el resultado a pantalla 
        if arguments.PRINT:
            print("Informacion obtenida del archivo\n")
            print(f"Name:\n\t{gb_record.name}\n")
            print(f"Date:\n\t{gb_record.annotations['date']}\n")
            print("Features:\n")
            print(f"\tOrganism: {' '.join(gb_record.features[0].qualifiers['organism'])}\n")
            print(f"\tCountry: {' '.join(gb_record.features[0].qualifiers['country'])}\n")
            print(f"\tIsolation source: {' '.join(gb_record.features[0].qualifiers['isolation_source'])}\n")
            print(f"\tLocation: {gb_record.features[0].location}\n\tType: {gb_record.features[0].type}\n")