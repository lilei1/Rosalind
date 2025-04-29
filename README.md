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

#solution:
```
python3 enu_kmer_lexi_recursive.py rosalind_lexv.txt >out
```
---

##problem
Rabbits and Recurrence Relations 
Problem
A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π)
 and the infinite sequence of odd numbers (1,3,5,7,9,…)
. We use the notation an
 to represent the n
-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn
 represents the number of rabbit pairs alive after the n
-th month, then we obtain the Fibonacci sequence having terms Fn
 that are defined by the recurrence relation Fn=Fn−1+Fn−2
 (with F1=F2=1
 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n
-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n
. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40
 and k≤5
.

Return: The total number of rabbit pairs that will be present after n
 months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair).

Sample Dataset
5 3
Sample Output
19

```
python3 wascallywabbits.py rosalind_fib.txt
20444528200
```
---

###
Finding a Most Likely Common Ancestorclick to collapse
In “Counting Point Mutations”, we calculated the minimum number of symbol mismatches between two strings of equal length to model the problem of finding the minimum number of point mutations occurring on the evolutionary path between two homologous strands of DNA. If we instead have several homologous strands that we wish to analyze simultaneously, then the natural problem is to find an average-case strand to represent the most likely common ancestor of the given strands.

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n
 matrix has m
 rows and n
 columns. Given a matrix A
, we write Ai,j
 to indicate the value found at the intersection of row i
 and column j
.

Say that we have a collection of DNA strings, all having the same length n
. Their profile matrix is a 4×n
 matrix P
 in which P1,j
 represents the number of times that 'A' occurs in the j
th position of one of the strings, P2,j
 represents the number of times that C occurs in the j
th position, and so on (see below).

A consensus string c
 is a string of length n
 formed from our collection by taking the most common symbol at each position; the j
th symbol of c
 therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

A T C C A G C T
G G G C A A C T
A T G G A T C T
DNA Strings	A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T
A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6
Consensus	A T G C A A C T
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

```

```

---
