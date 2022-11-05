'''
Name
    entrez_search.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que dado informacion genera un termino y hace un archivo de salida con bases de datos 
    asociados a sus IDs 
    
Category
    BioPython 
    
Usage
    Python entrez_search.py [-h] -f FILE -t TERM 
Ej. 
    py .\src\entrez_search.py -f "results/entrez_ids" -t "Drosophila: hox o emo, Ecoli: pitB o rcs"
    
Arguments
    -h --help
    -f --FILE
    -t --TERM
    
See also
    None
'''
from calendar import c
from contextlib import suppress
from dataclasses import field
from Bio import Entrez
from pprint import pprint
import argparse
Entrez.email = 'blopez.lcg.unam.mx'

arg_parser = argparse.ArgumentParser(description="Obtener IDs de una base de datos")

arg_parser.add_argument("-f", "--FILE",
                    help="Archivo de salida",
                    required=True)
                    
arg_parser.add_argument("-t","--TERM",
                    help = "Termino que deseas buscar: organismo: gene1 o gene2, organismo ...",
                    type = str,
                    required= True)
                    
arguments = arg_parser.parse_args()

# Es importante que el formato de los datos este dado de la siguiente forma:
# Drosophila: hox o emo, Ecoli: pitB o rcs

def make_term(termino):
    '''
    Funcion que toma una string con formato: "organismo: gene1 o gene3, organismo:gene3 y gene4"
    para generar un termino que pueda utilizarse con egquery, uniicamente para buscar genes asociados 
    a organismos. 
    Parameters:
        Termino (str): La informacion del termino que se va a generar con la funcion organismo: gene1 o gene2
    Returns:
        final_terms (list): Lista de terminos generados para egquery.  
    '''
    # Separamos la informacion mediante split para generar listas que contengan la informacion
    # de cada organismo que se va a buscar
    # Agregamos tambien los condicionales OR y AND
    proces = termino.replace(" o "," OR ").replace(" y "," AND ").split(",")
    proces = [element.split(":") for element in proces]
    string_final= []
    # Comenzamos a contruir el string que contendra el termino. 
    for element in proces:
        # Separamos en otras listas, dependiendo si estas contienen AND o OR 
        for genes in element[1:]:
            and_split = genes.split("AND")
            or_split = genes.split("OR")
            if len(and_split) > 1:
                gene_string = and_split[0] + "[Gene]" + " AND "
                for gene in and_split[1:]:
                    # Si es el utimo elemento de la lista, solo añadimos el gene.
                    if gene == and_split[-1]:
                        gene_string += gene + "[Gene]"
                    else:
                        gene_string += gene + "[Gene]" + " AND "
            if len(or_split) > 1:
                gene_string = or_split[0] + "[Gene]" + " OR "
                for gene in or_split[1:]:
                    if gene == or_split[-1]:
                        gene_string += gene + "[Gene]"
                    else:
                        gene_string += gene + "[Gene]" + " OR "   
            string_final.append(gene_string)
    
    # Obtenemos el organismo al que pertenece cada uno de los genes que procesamos 
    # para el string
    organisms = [element[0] for element in proces]
    string_final = [genes.split(",") for genes in string_final]
    #   Insetamos el organismo al inicio de cada lista. 
    none_list = [string_final[i].insert(0, organisms[i]) for i in range(0, len(organisms))]

    final_terms = []
    # Por ultimo, agregamos la informacion que se requiere para contruir el termino con el organismo.
    # Regresamos el termino final
    for organism in string_final:
        term = organism[0] + "[Orgn]" + " AND " + "("
        term += organism[1] + ")"
        final_terms.append(term)
    return(final_terms)

# Llamamos a la funcion.
terms = make_term(arguments.TERM)

def get_ids(terms, path):
    '''
    Funcion que obtiene los ID's con egquery y los escribe en un archivo. 
    Parameters:
        terms (list): lista que contiene a los terminos que seran utilizados 
        por egquery.
        path (str): ruta para el archivo de salida. 
    Returns:
        "file created" (message)
    '''
    # Abrimos el archivo que contendra la informacion.
    with open(path, "w") as file:
        for termino in terms:
            organism = termino.split("[Orgn]")
            organism = organism[0]
            # Agregamos un encabezado.
            file.write(f">{organism}\n")
            data_bases = []
            # Utilizamos el termino en egquery 
            handle = Entrez.egquery(term = termino)
            record = Entrez.read(handle)
            for row in record["eGQueryResult"]:
                # Solo buscamos en los row para los que el campo count es distinto de 0 y 
                # distinto de "error"
                # Añadimos las bases de datos a una lista.
                if row["Count"] != "0" and row["Count"]!= "Error":
                    data_bases.append(row["DbName"])
            for datab in data_bases:
                # Utilizamos try - except, ya que algunas veces habia problemas con las bases de 
                # datos y esto cortaba el proceso de busqueda para las demas bases.
                try:
                    # Utilizamos esearch para buscar el termino en cada base de datos guardada anteriormente 
                    # Escribimos esta informacion en un archivo.
                    db_handle = Entrez.esearch(datab, term= termino)
                    db_record = Entrez.read(db_handle)
                    handle.close()
                    file.write(f"{datab}:{' '.join(db_record['IdList'])}\n")
                except:
                    pass
        return("file created")

# Imrpimimos el mensaje a pantalla:
print(get_ids(terms, arguments.FILE))