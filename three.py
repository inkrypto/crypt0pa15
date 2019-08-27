#!/usr/bin/python

import string

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
english_frequencies = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01, 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

'''
given plaintext:
1. generate a frequency with which that char is used
2. for each char accumulate a difference from english
3. take the difference, that is the score
'''
def score(s):
	global english_freq
	generated_count = {}
	generated_frequency = {}
	score_count = 0
	# get the count and the frequency of the characters
	for i in s.lower():
		if i not in generated_count.keys():
			generated_count[i] = 1
			generated_frequency[i] = (1/float(len(s)) * 100)
		else:
			generated_count[i] += 1
			generated_frequency[i] = generated_count[i]/float(len(s)) * 100
	# score the characters 
	for i in generated_frequency.keys():
		if i in english_frequencies.keys():
			score_count += abs(english_frequencies[i] - generated_frequency[i])
		elif i in string.whitespace:
			score_count += 1
		elif i in string.punctuation[0:7]:
			score_count += 10
		elif i in string.printable:
			score_count += 15
		else:
			score_count += 18
	return abs(1000 - score_count)

def xor(s, k):
	r = ''
	for i in s:
		r += chr(ord(i) ^ ord(k))
	return r

def main():
	global ciphertext
	max_score = 0 
	max_string = ''
	for k in range(0, 256):
		key = chr(k)
		s = xor(ciphertext, key)
		sc = score(s)
		if sc > max_score:
			max_score = sc
			max_string = s
	print('Score = {}, Answer = {}'.format(str(max_score), max_string))

if __name__ == '__main__': main()

	
