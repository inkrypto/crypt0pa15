#!/usr/bin/python

import string

# the letter frequency of number of times a letter appears in a word
english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01, 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

# this function scores each character then subtracts the English character frequency from the plaintext frequency 
def score_text(plaintext):
	global english_freq
	generated_count = {}
	generated_frequency = {}
	score = 0				#penalize char frequency. garbage gets a low score, english get a high score
	for i in plaintext.lower():
		if i not in generated_count.keys():
			generated_count[i] = 1
			generated_frequency[i] = (1/float(len(plaintext))) * 100
		else:
			generated_count[i] += 1
			generated_frequency[i] = (generated_count[i]/float(len(plaintext))) * 100
	for i in generated_frequency.keys():
		if i in english_freq.keys():
			score += abs(english_freq[i] - generated_frequency[i])
		elif i in string.whitespace:
			score += 1
		elif i in string.punctuation[0:7]:
			score += 10
		elif i in string.printable:
			score += 15
		else:
			score += 18
	return abs(1000 - score)

