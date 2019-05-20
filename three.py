#!/usr/bin/python

'''
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
'''

from __future__ import print_function
import string

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

# frequency analysis
temp = {}
for i in range(0, len(a)):
	if a[i] in temp.keys():
		temp[a[i]] += 1
	else:
		temp[a[i]] = 1
print(temp)
print('')

# old algorithm
#brute forced every letter
#for x in range(0, len(a)):
#	print(chr(ord(a[x]) ^ ord('x')),end='')


# new algorithm
#for ever char in the alphabet xor the string with that alphabet letter as the key
for key in string.ascii_lowercase:
	print('running encrypt with key {}: '.format(key), end='')
	for character in range(0, len(a)):
		print(chr(ord(a[character]) ^ ord(key)), end='')
	print('')






























