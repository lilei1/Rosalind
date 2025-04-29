#!/usr/bin/env python3
import sys

#define a function to calculate the number of rabbit pairs
#n is the month and k is the number of rabbit pairs produced by each pair
def rabbit_pairs(n,k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs(n-1,k) + k*rabbit_pairs(n-2,k)
    
file = sys.argv[1]
with open (file, 'r') as F:
    n,k = map(int, F.readline().strip().split())
    print(rabbit_pairs(n,k))