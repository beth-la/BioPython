'''
Module name
    Aminoacids module

Description 
    Modulo que contiene funciones que nos permiten trabajar con secuencias de aminoacidos y cadenas 
    de ARN.
    
Version
    1.5
    
Author 
    Lopez A. Brenda E.

Functions
    aminoacid_per
    
''' 
import re 
def aminoacid_per(aminoacid_sequence, aminoacid_list = ['A','I','L','M','F','W','Y','V']):
    '''
    Calcula el porcentaje de aminoacidos en una seuencia 
        Parameters:
            aminoacid_sequence (str): secuencia de aminoacidos dada por el usuario
            aminoacid_list (list): aminoacidos a calcular el porcentaje, por default ['A','I','L','M','F','W','Y','V']
        
        Returns:
            percentage (float): porcentaje de aminoacidos 
    '''
    
    length = len(aminoacid_sequence)
    aminoacid_count = 0
    
    for i in range(0,len(aminoacid_list)):
        aminoacid_count += str(aminoacid_sequence).upper().count(str(aminoacid_list[i]).upper())
        
    percentage = (aminoacid_count * 100)/ length
    
    return(percentage)

def traducction(secuencia):
    '''
    Convierte una secuencia de ARN en una secuencia de aminoacidos.
        Parameters:
            arn_sequence (list): Lista de tripletes de ARN.
        Returns:
            peptid (str): Cadena de aminoacidos generada.
    '''
    peptid = []
    for codon in secuencia:
        # Ala 
        if codon == 'GCU' or codon =='GCC' or codon =='GCA' or codon =='GCG':
            peptid.append('A')
        # Cys
        if codon == 'UGU' or codon =='UGC':
            peptid.append('C')
        # Asp
        if codon == 'GAU' or codon == 'GAC':
            peptid.append('D')
        # Glu
        if codon == 'GAA' or codon == 'GAG':
            peptid.append('E')
        # Phe
        if codon == 'UUU' or codon == 'UUC':
            peptid.append('F')
        # Gly
        if codon == 'GGU' or codon =='GGC' or codon =='GGA' or codon =='GGG':
            peptid.append('G')
        # His
        if codon == 'CAU' or codon == 'CAC':
            peptid.append('H')
        # Ile
        if codon == 'AUU' or codon == 'AUC' or codon =='AUA':
            peptid.append('I') 
        # Lys
        if codon == 'AAA' or codon == 'AAG':
            peptid.append('k')
        # Leu
        if codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
            peptid.append('L')
        # Met
        if codon == 'AUG':
            peptid.append('M')
        # Asn
        if codon == 'AAU' or codon =='AAC':
            peptid.append('N')
        # Pro
        if codon == 'CCU' or codon =='CCC' or codon =='CCA' or codon =='CCG':
            peptid.append('P')
        # Gln
        if codon == 'CAA' or codon == 'CAG':
            peptid.append('Q')
        # Arg
        if codon == 'CGU' or codon =='CGC' or codon =='CGA' or codon =='CGG' or codon == 'AGA' or codon =='AGG':
            peptid.append('R')
        # Ser
        if codon == 'UCU' or codon =='UCC' or codon =='UCA' or codon =='UCG' or codon =='AGU' or codon =='AGC':
            peptid.append('S')
        # Thr
        if codon == 'ACU' or codon =='ACC' or codon =='ACA' or codon =='ACG':
            peptid.append('T')
        # Val
        if codon == 'GUU' or codon == 'GUC' or codon =='GUA' or codon =='GUG':
            peptid.append('V')
        # Trp
        if codon == 'UGG':
            peptid.append('W')
        # Tyr
        if codon == 'UAU' or codon == 'UAC':
            peptid.append('Y')
        # STOP
        if codon == 'UAA' or codon == 'UGA' or codon == 'UAG':
            peptid.append('-STOP-')
    return("".join(peptid))
    
def evaluate_rna(rna):
    '''
    Evalua si el archivo contiene algun caracter diferente a los permitidos [AUGC].
        Parameters:
            dna (str): secuencia de ARN a procesar.
        Returns:
            0 (int): si encuentra caracteres invalidos.
            1 (int): si no encuentra caracteres invalidos. 
    '''
    not_dna = re.finditer("[^AUGC]+", rna)
    matches = len([*re.finditer("[^AUGC]+", rna)])
    if matches:
        for invalid in not_dna:
            print(f"Existen caracteres invalidos: {invalid.group()} en las coordenadas: {invalid.span()}")
        return(0)
    else:
        return(1)

def codon_format(sequence): 
    '''
    Da formato de codones a una secuencia de ARN o ADN.
        Parameters:
            ARN (str): secuencia de ARN a formatear.
        Returns:
            codon_seq (list): lista con los codones de la secuencia. 
    '''
    codon_seq = [sequence[i:i+3] for i in range(0,len(sequence),3)]
    return(codon_seq)

def translate_dna(ADN):
    '''
    Convierte una secuencia de ADN a ARN.
        Parameters:
            ADN (str): secuencia de ADN a traducir.
        Returns:
            ARN_seq (str): secuencia de ARN. 
    '''
    ARN_dic = {'A' : 'U','T' : 'A','C' : 'G','G' : 'C'}
    ARN_seq = [ARN_dic.get(nucleotide) for nucleotide in ADN]
    return(''.join(ARN_seq))