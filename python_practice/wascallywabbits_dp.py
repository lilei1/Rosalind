#!/usr/bin/env python3

#this is to use the dynamic programming approach to solve the wascally wabbits problem
import sys

#define a function to calculate the number of rabbit pairs
#n is the month and k is the number of rabbit pairs produced by each pair
def rabbit_pairs(n,k):
    #create a list to store the number of rabbit pairs
    rabbit_pairs = [0] * (n+1) #Let me explain in more detail:[0] is a list containing a single zero; * (n+1) repeats this element n+1 times, So [0] * (n+1) creates a list like [0, 0, 0, ..., 0] with n+1 zeros
    #set the initial values
    rabbit_pairs[1] = 1
    rabbit_pairs[2] = 1
    #calculate the number of rabbit pairs
    for i in range(3, n+1):
        rabbit_pairs[i] = rabbit_pairs[i-1] + k*rabbit_pairs[i-2]
    return rabbit_pairs[n]

file = sys.argv[1]
with open (file, 'r') as F:
    n,k = map(int, F.readline().strip().split())
    print(rabbit_pairs(n,k))


