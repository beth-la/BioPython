from Bio import SeqIO
import argparse
genes = ['N','G']

for gb_record in SeqIO.parse("data/virus.gb","genbank"):
    for gene in genes:
        for features in gb_record.features: 
            if features.type == "gene":
                print(features.qualifiers["gene"])
            #if features.type == "gene" and features.qualifiers["gene"][0] == gene:
            #    print(f"Gene: {gene}")
            #    ADN = gb_record.seq[features.location.nofuzzy_start:features.location.nofuzzy_end]
            #    ARN = ADN[:15].transcribe()
            #    protein = ADN[:15].translate()
            #    print(protein)