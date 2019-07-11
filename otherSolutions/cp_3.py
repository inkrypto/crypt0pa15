#!/usr/bin/python
import string
'''
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
'''

ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html

english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01, 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

'''
given a plaintext:
1. generate a frequency distribution of characters char : percent freq
2. for each char in generated frequency accumulate a difference from english
3. take the difference and subtract from 100, this is the score 
'''
def score_plain(s):
	global english_freq
	generated_count = {}
	generated_freq = {}
	score_count = 0
	for c in s.lower():
		if c not in generated_count.keys():
			generated_count[c] = 1
			generated_freq[c] = (1/float(len(s))) * 100
		else:
			generated_count[c] += 1
			generated_freq[c] = (generated_count[c]/float(len(s))) * 100
	for c in generated_freq.keys():
		if c in english_freq.keys():
			score_count += abs(english_freq[c] - generated_freq[c])
		elif c in string.whitespace:
			score_count += 1 
		elif c in string.punctuation[0:7]:
			score_count += 10 
		elif c in string.printable:
			score_count += 15 
		else:
			score_count += 18 
	return abs(1000 - score_count)
		
def xor(s,k):
	r = ''
	for c in s:
		r += chr( ord(c) ^ ord(k) )
	return r

def niceify(s):
	ns = ''
	for c in s:
		if c in string.printable:
			ns += c
		else:
			ns += '<' + c.encode('hex') + '>'
	return ns

def main():
	global ct
	max_score = 0
	max_string = ''
	for k in range(0, 256):
		key = chr(k)
		s = xor(ct, key)
		sc = score_plain(s)
		if sc > max_score:
			max_score = sc
			max_string = s
		#if sc > 900: print('key {} SCORE : score: {}, string: {}'.format(str(k),str(sc),niceify(s)))
		#import pdb; pdb.set_trace()
	print('FINAL : score: {}, string: {}'.format(str(max_score),niceify(max_string)))

main()

