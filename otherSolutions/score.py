#!/usr/bin/python

import string

english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01, 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

def score_plain(plain_text):
	global english_freq
	generated_count = {}  	# determine the number of times a char is seen
	generated_freq = {}		# determine the number of occurences
	score_count = 0			# keep track to determine a score to penalize char freq. 
	for c in plain_text.lower():
		if c not in generated_count.keys():
			generated_count[c] = 1
			generated_freq[c] = 1/float(len(plain_text)) * 100
		else:
			generated_count[c] += 1
			generated_freq[c] = generated_count[c]/float(len(plain_text)) * 100

	print(generated_freq)
	print(generated_count)

def main():
	plaintext = 'super duper fucking leet shit man'
	score_plain(plaintext)
	print('hello')

if __name__ in '__main__': main()
