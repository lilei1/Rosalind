#!/usr/bin/env python3
import sys
from itertools import product

#define a function to generate all k-mers of length 1 to n with allowing the repeat of sinle base
def generate_kmers(n, alphabet):
    kmers = []
    for k in range(1, n+1):
        for p in product(alphabet, repeat=k):
            kmers.append(''.join(p))
    return kmers

file = sys.argv[1]
with open (file, 'r') as F:
    alphabet = F.readline().strip().split()
    n = int(F.readline().strip())

    kmers = generate_kmers(n, alphabet)
    for kmer in kmers:
        print(kmer)
