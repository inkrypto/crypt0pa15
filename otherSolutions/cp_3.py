#!/usr/bin/python
import string
import pdb
'''
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
'''

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html

english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01, 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

'''
given a plaintext:
1. generate a frequency distribution of characters char : percent freq
2. for each char in generated frequency accumulate a difference from english
3. take the difference and subtract from 100, this is the score 
'''
def score_plain(strng):
	global english_freq
	generated_count = {}
	generated_freq = {}
	score_count = 0						# penalize character frequency. garbage char=low score. english char=high score
	for chrtr in strng.lower():
		if chrtr not in generated_count.keys():
			generated_count[chrtr] = 1
			# use pdb here to see what this var is 
			generated_freq[chrtr] = (1/float(len(strng))) * 100 #how he know to put this in here? not looping freq 
		else:
			generated_count[chrtr] += 1
			generated_freq[chrtr] = (generated_count[chrtr]/float(len(strng))) * 100
	for chrtr in generated_freq.keys():
		if chrtr in english_freq.keys():
			score_count += abs(english_freq[chrtr] - generated_freq[chrtr])
		elif chrtr in string.whitespace:
			score_count += 1 
		elif chrtr in string.punctuation[0:7]:
			score_count += 10 
		elif chrtr in string.printable:
			score_count += 15 
		else:
			score_count += 18 
	return abs(1000 - score_count) # why are we doing this? why subtracting from 1000
		
def brentxor(strng, key):
	xor = ''
	for chrtr in strng:
		xor += chr( ord(chrtr) ^ ord(key) )
	return xor

# pretty print function
def niceify(strng):
	newstring = ''
	for chrtr in strng:
		if chrtr in string.printable:
			newstring += chrtr
		else:
			newstring += '<' + chrtr.encode('hex') + '>'
	return newstring

def main():
	global cont
	max_score = 0
	max_string = ''
	for key in range(0, 255):					# loop through all ascii 
		my_key = chr(key)						# key = each char looping through 0-255
		strng = brentxor(ciphertext, my_key)		# store return of brentxor in s
		score = score_plain(strng)					# store return of score plain if sc > max_score:
		if score > max_score:
			max_score = score					# update max score
			max_string = strng					# update max string
		#if sc > 900: print('key {} SCORE : score: {}, string: {}'.format(str(k),str(sc),niceify(s)))
		#import pdb; pdb.set_trace()
	print('FINAL : score: {}, string: {}'.format(str(max_score),niceify(max_string)))

main()

