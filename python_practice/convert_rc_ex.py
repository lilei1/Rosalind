#!/usr/bin/env python3
import sys
#define a function for convert the DNA sequence to the completary sequence
def convertRC(seq):
    seq=seq.upper()
    complement = {
        'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
        'Y': 'R', 'R': 'Y', 'S': 'S', 'W': 'W',
        'K': 'M', 'M': 'K', 'B': 'V', 'V': 'B',
        'D': 'H', 'H': 'D', 'N': 'N', 
        '-': '-', '?': '?'  # Gaps and unknown characters remain the same
    }
    seqrc =''
    for bp in reversed(seq):
        if bp in complement:
            seqrc += complement[bp]
        else:
            seqrc += bp 

    return seqrc

file = sys.argv[1]
dna_seq = ''
with open (file, 'r') as F:
    for line in F:
        line = line.strip()
        if not line.startswith('>'):
            dna_seq += line

print(convertRC(dna_seq))