#!/usr/bin/env python3

import sys

#define a function to find the motif
def find_motif(dna, motif):
    dna = dna.upper()
    motif = motif.upper()
    positions = []
    for i in range(len(dna)):
        if dna[i:i+len(motif)] == motif:
            positions.append(i+1)
    return positions

#read the input file
with open(sys.argv[1], 'r') as input_file:
    dna = input_file.readline().strip()
    motif = input_file.readline().strip()

#find the motif and print the positions
positions = find_motif(dna, motif)
print(' '.join(map(str, positions)))
