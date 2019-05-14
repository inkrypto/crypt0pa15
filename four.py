#!/usr/bin/python

'''
Detect single-character XOR 
One of the 60-character strings in this file has been encrypted by single-character XOR. Find it. 
(Your code from #3 should help.)
'''

with open('files/4.txt') as f:
	for line in f:
		print(line)


'''
Notes from Josh
-Read Markov frequency analysis
	-Determine the number of letters
	-if not letter
		-disregard
-write a function to determine if English
-use string ascii.lower + ascii.punctuation
-XOR has 255, 0-255
-store loop results in string 'temp = ""'
'''
