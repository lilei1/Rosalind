#write a function to generate all k-mers of length n
"""
    Generate all possible k-mers of length n from the given alphabet.
    
    Args:
        n: Length of each k-mer
        alphabet: List of characters to use (default: DNA nucleotides)
        
    Returns:
        List of all possible k-mers of length n
"""
def generate_kmers(n, alphabet=['A', 'C', 'G', 'T']):
    # Base case: if n is 0, return an empty string
    if n == 0:
        return ['']
    # Recursive case: get k-mers of length n-1, then add each letter from alphabet
    result = []
    for kmer in generate_kmers(n-1, alphabet):
        for base in alphabet:
            result.append(kmer + base)
    return result

print("1-mers with DNA alphabet:", generate_kmers(1))
print("2-mers with DNA alphabet:", generate_kmers(2))
print("3-mers with DNA alphabet:", generate_kmers(3))