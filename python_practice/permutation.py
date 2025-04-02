#!/usr/bin/env python3
import sys
from itertools import permutations

def permutation_seq(given_nb):
    given_nb=int(given_nb)
    nblist = list(range(1,given_nb+1))
    #seqnb = nblist.pop(0)
    permslist = list(permutations(nblist))

    return permslist

file =sys.argv[1]

with open (file,'r') as F:
    number = F.readline().strip()
    perm_list = permutation_seq(number)
    print (len(perm_list))
    for sublist in perm_list:
        print(' '.join(str(item) for item in sublist))