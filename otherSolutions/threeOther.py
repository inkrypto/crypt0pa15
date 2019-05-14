#!/usr/bin/python

from __future__ import print_function
import string
from collections import Counter

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
b = a.decode('hex')
c = string.ascii_lowercase
d = {}

print(a)
print(b)
print(c)

counts=Counter(a)
for i in b:
	print(i, counts[i], end='')

for x in range(0, len(b)):
	for y in range(0, len(c)):
		print(ord(b[x]) ^ ord(c[y]), end='')
