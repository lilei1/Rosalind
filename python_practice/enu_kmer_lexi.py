#!/user/bin/env python3
import sys
from itertools import product

def lexicographic_kmers(alphabet, k):
    # Generate all possible k-mers using Cartesian product
    kmers = [''.join(p) for p in product(alphabet, repeat=k)]
    return kmers

file = sys.argv[1]
with open (file, 'r') as F:
    alphabet = F.readline().strip().split()
    k = int(F.readline().strip())

    kmers = lexicographic_kmers(alphabet, k)
    for kmer in kmers:
        print(kmer)
