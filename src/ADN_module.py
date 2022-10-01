'''
Module name
    ADN module

Description 
    Modulo que contiene funciones que nos permiten trabajar con secuencias de ADN, contar y obtener 
    porcentajes de nucleotidos; obtener archivos en formato fasta, etc. 

Version
    1.0
    
Author 
    Lopez A. Brenda E.

Functions
    at_content
    count_dna
    delete_adapters 
    fasta_files
    gc_content
    nucleotide_percentage 
    
'''
import re
def count_dna(dna):
    '''
    Regresa el conteo de nucleotidos en una secuencia de ADN 
        Parameters:
            adn (str): secuencia de ADN a procesar
        Returns:
            adn_count (list): lista que contiene cuenta de nucleotidos en el siguiente orden: (A, T, G, C) 
    '''
    dna_count = []
    dna_count.append(dna.upper().count('A'))
    dna_count.append(dna.upper().count('T'))
    dna_count.append(dna.upper().count('G'))
    dna_count.append(dna.upper().count('C'))
    return(dna_count)

def at_content(pathfile, flag_round = 0):
    '''
    Regresa la proporcion de AT en una secuencia de ADN
        Parameters:
            pathfile (str): ruta del archivo que contiene la cadena de ADN a procesar
            flag_round (int): parametro opcional que permite redondear el resultado obtenido
        Returns:
            at_content (float): Proporcion de AT en la secuencia
    '''
    with open(pathfile, "r") as seq_file:
        my_dna = seq_file.read()
    
    length = len(my_dna) 
    a_count = my_dna.count('A') 
    t_count = my_dna.count('T')

    if flag_round:
        at_content = round((a_count + t_count) / length, flag_round)
    else:
        at_content = ((a_count + t_count) / length)
        
    return(at_content)

def gc_content(pathfile, flag_round = 0):
    '''
    Regresa la proporcion de GC en una secuencia de ADN
        Parameters:
            pathfile (str): ruta del archivo que contiene la cadena de ADN a procesar
            flag_round (int): parametro opcional que permite redondear el resultado obtenido
        Returns:
            gc_content (float): Proporcion de GC en la secuencia
    '''
    with open(pathfile, "r") as seq_file:
        my_dna = seq_file.read()
    
    length = len(my_dna) 
    g_count = my_dna.count('G') 
    c_count = my_dna.count('C')

    if flag_round:
        gc_content = round((g_count + c_count) / length, flag_round)
    else:
        gc_content = ((g_count + c_count) / length)
        
    return(gc_content)

def nucleotide_percentage(filepath):
    '''
    Obtiene el porcentaje de nucleotidos (AT y GC) en una secuencia de ADN
        Parameters:
            pathfile (str): ruta del archivo que contiene la cadena de ADN a procesar
        Returns:
            percentage (list): Lista que contiene el porcentage de aminoacidos en el siguiente orden: (AT, GC)
    '''  
    with open(filepath) as archivo:
        secuencia_adn  = archivo.read()
        longitud_secuencia = len(secuencia_adn)
        
    percentage = []
    percentage_AT = ((secuencia_adn.count('A') + secuencia_adn.count('T')) * 100 )/(longitud_secuencia)
    percentage_GC = (100 - percentage_AT)
    percentage.append(percentage_AT)
    percentage.append(percentage_GC)
    
    return(percentage)

def delete_adapters(filepath_in, filepath_out = "data/file_adapters"):
    '''
    Elimina adaptadores de una secuencia de ADN 
        Parameters:
            pathfile_in (str): ruta del archivo que contiene la cadena de ADN a procesar
            pathfile_out (str): ruta del archivo final en donde se escribiran las secuencias de ADN sin adaptadores
        Returns:
            filepath_out (str): ruta del archivo final
    '''
    with open(filepath_in,'r') as archivo:
        secuencias= [line for line in archivo]
        sin_adaptadores= []
    
    for i in range(0,len(secuencias)):
        sin_adaptadores.append(secuencias[i][14:])

    my_file= open(filepath_out,'w')
    my_file.write(''.join(sin_adaptadores))
    my_file.close()
    return(filepath_out)

def fasta_files(filepath_in, filepath_out = "data/fasta_file.fasta"):
    '''
    Genera un archivo con formato fasta.
        Parameters:
            filepath_in (str): ruta del archivo que contiene la secuencia de ADN 
            filepath_out (str): ruta del archivo final que contendra el formato fasta deseado
        Returns:
            filepath_out (str): ruta del archivo final
    '''
    with open(filepath_in, 'r') as archivo:
        secuencias = [line for line in archivo]
    
    format_seq = [secuencia[5:].upper().replace('-','') for secuencia in secuencias]

    my_file = open(filepath_out, 'w')
    
    for i in range(0,len(format_seq)):
        my_file.write(" > seq_" + str(i+1) + "\n" + format_seq[i])
    my_file.close()
    
    return(filepath_out)
    
def evaluate_dna(dna):
    '''
    Evalua si el archivo contiene algun caracter diferente a los permitidos [ATGC].
        Parameters:
            dna (str): secuencia de ADN a procesar.
        Returns:
            0 (int): si encuentra caracteres invalidos.
            1 (int): si no encuentra caracteres invalidos. 
    '''
    not_dna = re.finditer("[^ATGC]+", dna)
    matches = len([*re.finditer("[^ATGC]+", dna)])
    if matches:
        for invalid in not_dna:
            print(f"Existen caracteres invalidos: {invalid.group()} en las coordenadas: {invalid.span()}")
        return(0)
    else:
        return(1)
        
def complement_adn(ADN):
    '''
    Convierte una secuencia de ADN a su complemento.
        Parameters:
            ADN (str): secuencia de ADN a traducir.
        Returns:
            ARN_seq (str): secuencia de ARN. 
    '''
    ARN_dic = {'A' : 'T','T' : 'A','C' : 'G','G' : 'C'}
    ARN_seq = [ARN_dic.get(nucleotide) for nucleotide in ADN]
    return(''.join(ARN_seq))