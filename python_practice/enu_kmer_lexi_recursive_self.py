#!/usr/bin/env python3

import sys

def kmer_enu(k,alphabet):
	kmers = []
	if k == 0:
		return ['']
	else:
		for base in alphabet:
			for kmer in kmer_enu(k-1, alphabet):
				kmers.append(base+kmer)
		return kmers

#define the function of main

file = sys.argv[1]
with open (file, 'r') as f:
	alphabet = f.readline().strip().split()
	k = int(f.readline().strip())

	kmers = kmer_enu(k,alphabet)
	for kmer in kmers:
		print(kmer)
