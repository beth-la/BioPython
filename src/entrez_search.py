'''
Name
    GenBank_search.py
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion

    
Category
    GenBank 
    
Usage

Arguments
    -h --help
    -f --FILE
    -o --OUTPUT 
    -p --PRINT
    -g --GENES
    
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

arg_parser.add_argument("-p","--PRINT",
                    help = "Imprimir a pantalla los datos obtenidos",
                    action = 'store_true',
                    required= False)
                    
arg_parser.add_argument("-t","--TERM",
                    help = "Termino que deseas buscar",
                    type = str,
                    required= True)
                    
arguments = arg_parser.parse_args()

def make_term(termino):
    proces = termino.replace(" o "," OR ").replace(" y "," AND ").split(",")
    proces = [element.split(":") for element in proces]
    string_final= []
    for element in proces:
        for genes in element[1:]:
            and_split = genes.split("AND")
            or_split = genes.split("OR")
            if len(and_split) > 1:
                gene_string = and_split[0] + "[Gene]" + " AND "
                for gene in and_split[1:]:
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

    organisms = [element[0] for element in proces]
    string_final = [genes.split(",") for genes in string_final]
    none_list = [string_final[i].insert(0, organisms[i]) for i in range(0, len(organisms))]

    final_terms = []
    for organism in string_final:
        term = "'" + organism[0] + " AND " + "("
        term += organism[1] + ")'"
        final_terms.append(term)
    return(final_terms)
    
terms = make_term(arguments.TERMINO)

def get_ids(terms, path):
    with open(path, "w") as file:
        for termino in terms:
            organism = termino.split("[Orgn]")
            organism = organism[0]
            file.write(f"Organism: {organism}\n")
            data_bases = []
            handle = Entrez.egquery(term = termino)
            record = Entrez.read(handle)
            for row in record["eGQueryResult"]:
                if row["Count"] != "0" and row["Count"]!= "Error":
                    data_bases.append(row["DbName"])
            for datab in data_bases:
                try:
                    db_handle = Entrez.esearch(datab, term= termino)
                    db_record = Entrez.read(db_handle)
                    handle.close()
                    file.write(f"\tData base: {datab}\n\t\tIDs: {' '.join(db_record['IdList'])}\n")
                except:
                    pass
        return("file created")
        
get_ids(terms, arguments.FILE)