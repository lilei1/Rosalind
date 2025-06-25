#!/user/bin/env python3

import sys

#read the file

with open (sys.argv[1],"r") as file:
	text = file.readline().strip()


#write a function to find the longest repeat in the text

def find_longest_repeat(text):
	longest = ''
	for i in range(len(text)):
		for j in range(i+1,len(text)):
			if text[i:j] in text[j:]:
				if len(text[i:j]) > len(longest):
					longest = text[i:j]

	return(longest)

print(find_longest_repeat(text))