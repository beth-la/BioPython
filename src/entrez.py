from dataclasses import field
from Bio import Entrez
from pprint import pprint
Entrez.email = 'blopez.lcg.unam.mx'

#handle= Entrez.einfo(db= "protein")
#record = Entrez.read(handle)

#for field in record["DbInfo"]["FieldList"]:
#    if "UID" == field['Name']:
#        print(field['Description'])

#for field in record["DbInfo"]["LinkList"]:
#    if "protein_protein_small_genome" == field["Name"]:
#        print(field["Description"])

#termino = "(Drosophila[Title] OR Ecoli[Title]) AND transcriptome[Title]"
#handle = Entrez.esearch(db= "pubmed", term = "termino")
#result = Entrez.read(handle)

#IDs = result["IdList"]#
# print(IDs)

handle = Entrez.einfo()
record_db = Entrez.read(handle)
for db in record_db['DbList']:
    handle = Entrez.einfo(bd=db)
    record_db = Entrez.read(handle)
    db_field = record_db['DbInfo']
    
#    if "protein" in db_field:
#        chosen = db 

#new_handle = Entrez.einfo(db= chosen)
#record = Entrez.read(new_handle)
#for field in record['DbInfo']['FieldList']:
#    field_desc = field['description'].lower()
#    print(field_desc)