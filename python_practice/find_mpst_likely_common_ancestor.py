#!/usr/bin/env python3
#This is to find the most likely common ancestor of a set of sequences. the input sequences are in a fasta format,
# and the output a matrix of count number of each base at each position in the sequences across the sequences.
import sys

#calculate the profile matrix and consensus
def profile_matrix(sequences):
    #get the length of the sequences
    length = len(sequences[0])

    #Verify all sequences have the same length
    for sequence in sequences:
        if len(sequence) != length:
            raise ValueError('All sequences must have the same length')
        
    #create a dictionary to store the count of each base at each position
    profile = {'A': [0]*length, 'C': [0]*length, 'G': [0]*length, 'T': [0]*length}
    #loop through the sequences
    for sequence in sequences:
        #loop through the bases in the sequence
        for i in range(min(len(sequence), length)):
            base = sequence[i]
            if base in profile:
                #add the count of the base at the position to the profile
                profile[sequence[i]][i] += 1
    #create a list to store the consensus
    consensus = ''
    #loop through the positions
    for i in range(length):
        #find the base with the highest count at the position
        max_base = max(profile, key=lambda x: profile[x][i])
        #add the base to the consensus
        consensus += max_base
    #return the profile and consensus
    return profile, consensus

#read the sequences from the file
sequences = []
current_seq = ""
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line: 
            continue
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
            current_seq = ''
        else:
            current_seq += line
    #don't forget the last sequence   
    if current_seq:
        sequences.append(current_seq)

#calculate the profile matrix and consensus
profile, consensus = profile_matrix(sequences)

#print the consensus
print(consensus)
#print the profile matrix
for base in profile:
    print(base + ':', ' '.join(str(x) for x in profile[base]))  
