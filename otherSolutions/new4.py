#!/usr/bin/python
'''
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
'''

import string
from xor import xor
from score import score_text

def main():
	file_obj = ''
	cipherlist = []
	with open('files/4.txt') as f:
		for line in f:
			cipherlist.append(line.strip().decode('hex'))

	max_score = 0
	max_string = ''

	for k in range(0, 255):
		key = chr(k)
		for i in cipherlist:
			x = xor(i, key)
			sc = score_text(x)
			if sc > max_score:
				max_score = sc
				max_string = x
	print('Final score: {}, string: {}'.format(str(max_score), max_string))

if __name__ == '__main__': main()
