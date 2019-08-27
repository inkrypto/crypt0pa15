#!/usr/bin/python

def xor(ciphertext, key):
	x = ''
	for i in ciphertext:
		x += chr(ord(i) ^ ord(key))
	return x 
