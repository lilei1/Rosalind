#!/usr/bin/env python3
import sys

def print_lexicographic_kmers(alphabet, k):
    def backtrack(prefix):
        # Print prefix if it is non-empty
        if prefix:
            print(prefix)
        # If we can still extend, recurse
        if len(prefix) < k:
            for symbol in alphabet:
                backtrack(prefix + symbol)

    # Start from empty prefix
    backtrack("")

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as F:
        # First line has the alphabet (e.g., "D N A")
        alphabet = F.readline().strip().split()
        # Second line has the integer k
        k = int(F.readline().strip())
    
    print_lexicographic_kmers(alphabet, k)