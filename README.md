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

Problem 4
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540

Problem 5: 
Evolution as a Sequence of Mistakesclick to expand
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s
 and t
 of equal length, the Hamming distance between s
 and t
, denoted dH(s,t)
, is the number of corresponding symbols that differ in s
 and t
. See Figure 2.

Given: Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
.

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output

---

###Organizing Strings of Different Lengthsclick to expand
Problem
Say that we have strings s=s1s2⋯sm
 and t=t1t2⋯tn
 with m<n
. Consider the substring t′=t[1:m]
. We have two cases:

If s=t′
, then we set s<Lext
 because s
 is shorter than t
 (e.g., APPLE<APPLET
).
Otherwise, s≠t′
. We define s<Lext
 if s<Lext′
 and define s>Lext
 if s>Lext′
 (e.g., APPLET<LexARTS
 because APPL<LexARTS
).
Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜
 and a positive integer n
 (n≤4
).

Return: All strings of length at most n
 formed from 𝒜
, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

Sample Dataset
D N A
3
Sample Output
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA

---

