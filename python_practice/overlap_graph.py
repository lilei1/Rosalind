#!/usr/bin/env python3

import sys

#write the overlap graph function
def overlap_graph(reads, k):
    #create a dictionary to store the reads
    reads_dict = {}
    #loop through the reads
    for read in reads:
        #add the read to the dictionary
        reads_dict[read] = []
        #loop through the reads
        for read2 in reads:
            #if the read is not the same as the read2
            if read != read2:
                print(f"Comparing {read} and {read2}")
                #if the last k-1 characters of the read are the same as the first k-1 characters of the read2
                if read[-(k-1):] == read2[:k-1]:
                    print(f"Found overlap: {read} -> {read2}")
                    #add the read2 to the dictionary
                    reads_dict[read].append(read2)
                    print(f"Overlaps: {reads_dict}")
    #return the dictionary
    return reads_dict

#write the function to read the fasta file
def read_fasta(filename):
    #create a dictionary to store the IDs and reads
    reads_dict = {}
    current_ID = ""
    current_read = ""
    #open the file
    with open(filename, 'r') as f:
        #loop through the file
        for line in f:
            #strip the line 
            line = line.strip()
            #if the line starts with a >
            if line[0] == '>':
                if current_ID and current_read:
                    reads_dict[current_ID] = current_read
                current_read = ""
                current_ID = line[1:]
            else:
            #add the line to the list
                current_read += line
        #don't forget the last read        
        if current_ID and current_read:        
            reads_dict[current_ID] = current_read
    #return the dictionary
    return reads_dict

#write print function
def print_overlap_graph(reads,k):
    overlaps = overlap_graph(reads,k)
    #loop through the dictionary
    for read1, read2s in overlaps.items():
        #loop through the reads
        for read2 in read2s:
            print(f"{read1} {read2}")

if __name__ == "__main__":
    #get the filename from the command line
    filename = "python_practice/" + sys.argv[1]
    #get the k from the command line
    k = int(sys.argv[2])
    #read the fasta file
    reads = read_fasta(filename)
    print(f"Parsed {len(reads)} reads from {filename}")
    #print the overlap graph
    print(f"Finding overlaps of length {k}...")
    print_overlap_graph(reads,k)

