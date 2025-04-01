#!/usr/bin/env python3
import sys

#define a convert function
def dna2rna(seq):
    rna = seq.replace('T','U')
    return rna

file = sys.argv[1]

dna_seq = ""
with open (file,'r') as F:
    for line in F:
        line =line.strip()
        if not line.startswith('>'):
            dna_seq += line
            
print (dna2rna(dna_seq))