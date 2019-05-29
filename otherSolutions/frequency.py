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

with open('../files/4.txt') as f:
	for line in f:
		temp += line.strip() 	# had to strip CRLF and newlines

a = temp.decode('hex')			# hex to ascii

freq = {}						# empty list to count char frequency

for i in range(0, len(a)):
	if a[i] in freq.keys():
		freq[a[i]] += 1			# increment number of times char used
	else:
		freq[a[i]] = 1

total_characters = len(a)
percentile = {}
high_percentile = {}
for i in freq.keys():
	percentile[i] = (freq[i] / float(total_characters)) * 100
	if percentile[i] > 1.0:
		high_percentile[i] = percentile[i]

freq_file = open('freq.txt', 'w')
freq_file.write(repr(freq))
freq_file.close()

percent_file = open('percent.txt','w')
percent_file.write(repr(high_percentile))
percent_file.close()
