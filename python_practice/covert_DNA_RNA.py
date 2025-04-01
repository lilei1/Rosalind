#!/usr/bin/env python3
import sys

#define a convert function
def dna2rna(seq):
    rna = seq.replace('T','U')
    return rna

file = sys.argv[1]

with open (file,'r') as F:
    for line in F:
        if line.startswith('>'):
            next;
        else:
            line += line
            
    print (dna2rna(line))