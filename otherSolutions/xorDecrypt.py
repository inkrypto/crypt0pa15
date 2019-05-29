#!/usr/bin/python

ciphertext = 'ETAOIN SHRDLU'

x = ''

for key in range(0, len(ciphertext)):
	x = x + chr(ord(ciphertext[key]) ^ ord('x'))

x = x.decode('hex')
print(x)

