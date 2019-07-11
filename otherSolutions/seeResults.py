#!/usr/bin/python

from __future__ import print_function
import string

english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01 , 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

def score_plain(s):
        global english_freq
        generated_count = {}
        generated_freq = {}
        score_count = 0 # penalize the distant between plaintext and english. the greater the distants the greater the penalty. garbage to have small score. english to have a high score. keep score of how 'englishness' a string is
        for c in s.lower():
                if c not in generated_count.keys():
                        generated_count[c] = 1
                        generated_freq[c] = (1/float(len(s))) * 100 # what % of the character is used
                else:
                        generated_count[c] += 1
                        generated_freq[c] = (generated_count[c]/float(len(s))) * 100
        for c in generated_freq.keys():
                if c in english_freq.keys():
                        score_count += abs(english_freq[c] - generated_freq[c]) # understand the distance of a given character in plaintext to the english frequency
                elif c in string.whitespace:
                        score_count += 1
                elif c in '!"&\'.:;?':  # adding the realistic uses of punctuation
                        score_count += 10
                elif c in string.printable: # if not a used char then gets a higher penalty
                        score_count += 15
                else:
                        score_count += 18 	# this definitely gets penalized
        return abs(1000 - score_count)

def brentxor(ciphertext, key):
	
	plaintext = ''
	for i in range(0, len(ciphertext)):
		plaintext += (chr(ord(ciphertext[i])^ord(key)))	
	return plaintext

def niceify(us):
	ns = ''
	for c in us:
		if c in string.printable:
			ns += c
		else:
			ns += '<' + c.encode('hex') + '>'
	return ns

def main():
	
	file_obj = ''

	with open('../files/4.txt') as f:
		for line in f:
			file_obj += line.strip() #strip because CRLF

	ciphertext = file_obj.decode('hex')

	# make file_obj list, 60 char stings for each index
	cipherlist = []
	for i in range(0, len(ciphertext)):
		if i % 60 == 0:
			cipherlist.append(ciphertext[i])
		else:
			cipherlist[-1] += ciphertext[i]
	
	#key = '5' 
	#print(niceify(brentxor(cipherlist[85], key))) 
	
	for ndices in range(0, len(cipherlist)):
		
		s = brentxor(cipherlist[ndices], key)
		print(niceify("ndx: {} plain: ".format(ndices) + brentxor(cipherlist[ndices],key))) # a print to use here
	
	print(score_plain(s))

if __name__ == '__main__':
	main()
