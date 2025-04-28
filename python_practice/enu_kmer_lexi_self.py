#!/usr/bin/env python3

import sys
from itertools import product

#use the cartesian product way to do kmer
def kermer_recurise(alphabet,k):
	kmers = [''.join(p) for p in product(alphabet, repeat=k)]
	return kmers

#define main function

file = sys.argv[1]
with open (file, 'r') as f:
	alphabet = f.readline().strip().split()
	k = int(f.readline().strip())
	kmers = kermer_recurise(alphabet,k)
	for kmer in kmers:
		print(kmer)

