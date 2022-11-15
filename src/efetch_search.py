'''
Name
    efetch search
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que obtiene el nombre de articulos a partir de sus IDs
    
Category
    Biopython
    
Usage
    Python efetch_search.py [-h] -f path/to/file -o OUTPUT
    
Arguments
    -h --help
    -f --FILE
    -o --OUTPUT 
    
See also
    None
'''
from ctypes.wintypes import HANDLE
from Bio import Entrez
import argparse
import re
from Bio import SeqIO

Entrez.email = 'blopez.lcg.unam.mx'
arg_parser = argparse.ArgumentParser(description="Obtener titulos y IDs de artuculos de bases de datos pubmed y pmc")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="Archivo que contiene los IDs a buscar",
                    required=True)
                    
arg_parser.add_argument("-o", "--OUTPUT",
                    help="Ruta para el archivo de salida",
                    required=True)
                    
arguments = arg_parser.parse_args()

def names_file(input, output):
    '''
    Toma un archivo con IDs asociados a bases de datos y utiliza aquellos que pertenecen a las bases de 
    datos pubmed o pmc para obtener los nombres de sus articulos.
    Parameters:
        input (str): Ruta hacia el archivo de entrada que contiene la informacion.
        output (str): Ruta del archivo de salida.
    Returns:
        message (str): mensaje para el usuario
    '''
    # Extraemos la informacion del archivo
    with open(input, "r") as archivo:
        information = archivo.read()
    
    # Le damos formato de lista 
    my_list = information.split(">")
    my_list = [element.split("\n") for element in my_list]
    my_list.pop(0)
    none = [element.pop(-1) for element in my_list]
    next = 0
    
    with open(output, "w") as output:
        # Recorremos la lista segun la informacion de cada organismo 
        for organism in my_list:
            db_ids= []
            list_article = []
            names= []
            count = 0
            output.write(f"Organism: {organism[0]}\n")
            
            # Recorremos cada base de datos
            for db in organism[1:]:
                db_name_id = db.replace(" ",",").split(":")
                # Solo nos interesan las base de datos pubmed y pmc
                if db_name_id[0] == "pubmed" or db_name_id[0] == "pmc":
                    db_ids.append(db_name_id)
                # Con entrez obtenemos el abstract de los articulos.
                    handle = Entrez.efetch(db= db_name_id[0], id=db_name_id[1], rettype="abstract", retmode="text")
                    read_myhandle = handle.read()
                    list_article.append(read_myhandle.split("\n\n"))
            for element in list_article:
                for information in element:
                    get_info = information.split("\n")
                    # Solo entra cuando la variable bandera es verdadera, añadiendo al elemento a la lista.
                    if next:
                        names.append(get_info[0])
                        next = 0
                    for posible_name in get_info:
                        # Los articulos de pubmed se encuentran enumerados, por lo que podemos utilizar esta estructura para parsear los datos 
                        if re.search("^\d+:", posible_name):
                            get_name = posible_name.split(": ")
                            names.append(get_name[1])
                        # Los articulos de pmc no tienen una estructura definida en su titulo, pero si en los 
                        # datos de sus fechas, estando enumerados, posterior a este patron viene el nombre 
                        # por lo que la variable next cambia de valor como un variable bandera.
                        if re.search("^\d{1,2}\.\s", posible_name):
                            next = 1
                            
            # Escribimos la informacion en el archivo
            output.write("\tArticles:\n")
            for name in names: 
                count += 1
                try:
                    output.write(f"\t\t{count}. {name}\n")
                except:
                    pass

            output.write("\tIDs de articulos que han citado a los articulos anteriores:\n")
            # Obtenemos los ids con entrez.link 
            for db_id in db_ids:
                output.write(f"\tData base:{db_id[0]}\n")
                record = Entrez.read(Entrez.elink(dbfrom=db_id[0], id=db_id[1],db=db_id[0]))
                cite_ids = [id["Id"] for id in record[0]["LinkSetDb"][0]["Link"]]
                output.write(f"\t{','.join(cite_ids)}\n")
    return("file created")

# Llamamos a la funcion
print(names_file(arguments.FILE, arguments.OUTPUT))