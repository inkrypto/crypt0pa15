#!/usr/bin/python

'''
Detect single-character XOR 
One of the 60-character strings in this file has been encrypted by single-character XOR. Find it. 
(Your code from #3 should help.)
'''

from __future__ import print_function
import string

# empty string to buffer file
temp = ''

with open('files/4.txt') as f:
	for line in f:
		temp += line.strip() 	# had to strip CRLF and newlines

a = temp.decode('hex')			# hex to ascii
freq = {}						# empty list to count char frequency
for i in range(0, len(a)):
	if a[i] in freq.keys():
		freq[a[i]] += 1			# increment number of times char used
	else:
		freq[a[i]] = 1

for i in freq:
	if freq[i] >= 100:
		print('key:{} frequency:{}'.format(repr(i), freq[i]))

# writing this next bit to a file because easier to read
solution = open('files/fourAnswer.txt', 'w')

# string of ascii chars
d = string.printable

for key in d:
	solution.write('encrypting with key {}: \n'.format(key))
	for i in range(0, len(a)):
		solution.write(chr(ord(a[i]) ^ ord(key)))
	solution.write('----End. \n')
solution.close()

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
