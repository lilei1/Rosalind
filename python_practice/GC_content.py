#!/usr/bin/env python3
import sys
#write a function to calculate the GC content for a sequence
def GC_content(seq):
    #GC_frac = ''
    seq = seq.upper()
    G_count = seq.count('G')
    C_count = seq.count('C')
    if len(seq) != 0:
        GC_frac = 100 * (G_count + C_count)/len(seq)
    else:
        GC_frac = 0 
    return GC_frac

file =sys.argv[1]
current_id = ''
current_seq = ''
GC_dict = {}
#GC_con =0
with open (file, 'r') as F:
    for line in F:
        line =line.strip()
        if line.startswith('>'):
            #save the previous sequence before moving to a new one
            if current_id and current_seq:
                GC_dict[current_id] = GC_content(current_seq)
                #GC_dict[current_id] = current_seq
            #seqID = line.replace('>','')
        #else:
        #start a new sequence
            current_id =line[1:] #remove the ">" 
            current_seq = ''
        else:
            current_seq += line
    #don' forgot to process the last sequence
    if current_id and current_seq:
        GC_dict[current_id] = GC_content(current_seq)
        #GC_dict[current_id] = current_seq

#print (GC_dict)
max_value = max(GC_dict.values())
max_keys = [key for key, value in GC_dict.items() if value == max_value][0]

print(max_keys)
print(f"{max_value:.6f}")