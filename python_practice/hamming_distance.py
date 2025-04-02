#!/usr/bin/env pyton3
import sys

#define a function to calculate the hamming distance
def dH_calculator(seq1, seq2):
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    #index1=0
    #index2=0
    count =0
    for i in range (len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1

    return count

file = sys.argv[1]

with open (file, 'r') as F:
    seq = []
    for line in F:
        line = line.strip()
        seq.append(line)
    
seq1 = seq[0]
seq2 = seq[1]
print(dH_calculator(seq1, seq2))
