#!/usr/bin/env python3
import sys
def count_bp(seq):
    seq = seq.upper()
    bp_count={}
    a = seq.count ('A')
    t = seq.count ('T')
    c = seq.count ('C')
    g = seq.count ('G')
    bp_count = {'A':a,'C':c,'G':g,'T':t}
    return bp_count

file_path = sys.argv[1]
with open(file_path,'r') as F:
    for line in F:
        if line.startswith('>'):
            next;
        else:
            line += line

    print(count_bp(line))
