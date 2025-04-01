#!/usr/bin/env python3
import sys
#define a function for convert the DNA sequence to the completary sequence
def convertRC(seq):
    seq=seq.upper()
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    seqrc = ''.join(complement[base] for base in reversed(seq))
    return seqrc

file = sys.argv[1]
dna_seq = ''
with open (file, 'r') as F:
    for line in F:
        line = line.strip()
        if not line.startswith('>'):
            dna_seq += line

    print(convertRC(dna_seq))