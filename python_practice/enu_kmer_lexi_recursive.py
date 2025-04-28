#!/user/bin/env python3
import sys
#from scratch using recursive way to do!!!!

def lexicographic_kmers(alphabet, k):
    if k == 0:
        return ['']
    else:
        kmers = []
        for base in alphabet:
            for kmer in lexicographic_kmers(alphabet, k-1):
                kmers.append(base + kmer)
        return kmers
    
file = sys.argv[1]
with open (file, 'r') as F:
    alphabet = F.readline().strip().split()
    k = int(F.readline().strip())

    kmers = lexicographic_kmers(alphabet, k)
    for kmer in kmers:
        print(kmer) 