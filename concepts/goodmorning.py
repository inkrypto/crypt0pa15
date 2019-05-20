#!/usr/bin/python
from __future__ import print_function
a = 'WVWWWUSQWWVSWWXWWV'
#b = a.encode('hex')
z = ''
for i in range(0, len(a)):
	z=chr(ord(a[i]) ^ ord('a'))
print(z)
