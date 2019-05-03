#!/usr/bin/python

message = 'no sleep til . . . '
translated = ''

i = len(message) - 1
while i >= 0:
	translated += message[i]
	i -= 1

print(translated)
print

encrypted = ' . . . lit peels on'
translated = ''
j = len(encrypted) - 1
while j >= 0:
	translated += encrypted[j]
	j -= 1

print(translated)
