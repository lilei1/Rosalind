# Rosalind
This is for practice to coding to solve bioinformatics problems

Problem 1
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output
20 12 17 21


Problem2: 

The Second Nucleic Acidclick to expand
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU


#problem3:

The Secondary and Tertiary Structures of DNAclick to expand
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT

