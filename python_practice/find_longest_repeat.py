#!/user/bin/env python3
import sys

#read the input file
with open(sys.argv[1], 'r') as input_file:
    text = input_file.readline().strip()

#find the longest repeat
def longest_repeat(text):
    longest = ''
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            if text[i:j] in text[j:]:
                if len(text[i:j]) > len(longest):
                    longest = text[i:j]
    return longest

print(longest_repeat(text))