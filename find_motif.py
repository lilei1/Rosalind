#!/usr/bin/env python3
import sys
import re

"""
This is for finding the motif in a protein sequence.
The motif is N{P}[ST]{P}, where N is any amino acid except P, {P} is any amino acid except P, [ST] is either S or T.
"""

#define a function to find the motif
def find_motif(protein):
    motif = re.compile('N[^P][ST][^P]')
    positions = []
    for i in range(len(protein)):
        if motif.match(protein[i:]):
            positions.append(i+1)
    return positions

#read the input file
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        line = line.strip()
        if line:
            positions = find_motif(line)
            if positions:
                print(line)
                print(' '.join(map(str, positions))) 
   
