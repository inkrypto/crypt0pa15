#!/usr/bin/python

from __future__ import print_function
import string

#empty string buffer for file
file_obj = ''

with open('../files/4.txt') as f:
	for line in f:
		file_obj += line.strip() #strip because CRLF

#decode hex
a = file_obj.decode('hex')

#make file_obj list, 60 char stings for each index
cipherlist = map(''.join, zip(*[iter(a)]*60))	

def brentxor(ciphertext, key):
	
	plaintext = ''
	for x in range(0, len(ciphertext)):
		for y in range(0, len(ciphertext[x])):
			for z in (ciphertext[y]):
				plaintext += (chr(ord(z)^ord(key)))	
	
	return plaintext

print(brentxor(cipherlist, 'x'))


#this prints list into dict
#alist = {i : cipherlist[i] for i in range(0, len(cipherlist))}

'''
#frequence analysis over list
frequencies = []
for x in cipherlist:
	frequencies.append({})
	frequency = frequencies[-1]
	for i in range(0, len(x)):
		if x[i] in frequency.keys():
			frequency[x[i]] += 1
		else:
			frequency[x[i]] = 1
print('String={}\n Frequencies={}'.format(repr(cipherlist[0]), frequencies[0]), end='')


total_characters = len(a)
percent = {}
high_percent = {}
for i in frequency.keys():
	percent[i] = (frequency[i] / float(total_characters)) * 100
	if percent[i] > 0.1:
		high_percent[i] = percent[i]

print(high_percent)

# written using ASCII
# chr(27) is escape character
# char(97) is letter 'a'
s = chr(27) + chr(97)

if s.isprintable() == True:
  print('Printable')
  else:
    print('Not Printable')
	  
	  s = '2+2 = 4'

	  if s.isprintable() == True:
	    print('Printable')
		else:
		  print('Not Printable'
'''
