#!/usr/bin/env python3
import sys
import re
import urllib.request
import ssl
import time

"""
This is for finding the motif in a protein sequence.
The motif is N{P}[ST]{P}, where N is any amino acid except P, {P} is any amino acid except P, [ST] is either S or T.
"""

def get_protein_sequence(uniprot_id):
    """Fetch protein sequence from UniProt."""
    # Extract the ID part before the underscore if it exists
    if '_' in uniprot_id:
        uniprot_id = uniprot_id.split('_')[0]
    
    # Create a context that doesn't verify certificates
    context = ssl._create_unverified_context()
    
    # Use the current REST API endpoint
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    try:
        with urllib.request.urlopen(url, context=context) as response:
            fasta = response.read().decode('utf-8')
            lines = fasta.strip().split('\n')
            # Skip the header line and join the sequence lines
            sequence = ''.join(lines[1:])
            return sequence
    except Exception as e:
        print(f"Failed to fetch sequence for {uniprot_id}: {e}")
        return None

def find_motif(protein):
    """Find the N-glycosylation motif in a protein sequence."""
    # N{P}[ST]{P} means: N followed by any amino acid except P, 
    # followed by either S or T, followed by any amino acid except P
    motif = re.compile('N[^P][ST][^P]')
    positions = []
    for i in range(len(protein) - 3):
        if motif.match(protein[i:i+4]):
            positions.append(i+1)
    return positions

# Read the input file containing UniProt IDs
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        uniprot_id = line.strip()
        if uniprot_id:
            protein_sequence = get_protein_sequence(uniprot_id)
            if protein_sequence:
                positions = find_motif(protein_sequence)
                if positions:
                    print(uniprot_id)
                    print(' '.join(map(str, positions)))
            # Add a small delay to avoid overwhelming the server
            time.sleep(0.5)
   
