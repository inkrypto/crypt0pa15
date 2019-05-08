#!/usr/bin/python

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

a = s1.decode('hex')
b = s2.decode('hex')

#to get answer
for x in range(0, len(a)):
	print(hex(ord(a[x]) ^ ord(b[x])))

#to get what answer is
for x in range(0, len(a)):
	print(chr(ord(a[x]) ^ ord(b[x])))
