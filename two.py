#!/usr/bin/python

def xor(s1, s2):
	x = ''
	for i in range(0, len(s1)):
		x += (chr(ord(s1[i]) ^ ord(s2[i])))
	return(x)

if __name__ == '__main__': 
	a = '1c0111001f010100061a024b53535009181c'
	b = '686974207468652062756c6c277320657965'
	s1 = a.decode('hex')
	s2 = b.decode('hex')
	print(xor(s1, s2))
