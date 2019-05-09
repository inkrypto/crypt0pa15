#!/usr/bin/python3
'''
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
'''

import sys

def xord(str1, str2):
	a = int(str1, 16)
	b = int(str2, 16)
	return (a ^ b)

def main():
	if len(sys.argv) != 3:
		print("Usage: two3.py string1 string2. For this challenge copy paste the strings from above")
		sys.exit(1)
	
	str1 = sys.argv[1]
	str2 = sys.argv[2]
	
	print(hex(xord(str1, str2)))

if __name__ == '__main__': main()


