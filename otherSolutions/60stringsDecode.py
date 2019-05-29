#!/usr/bin/python

from __future__ import print_function
import string

def charfreq(ciphertext):
	
	frequencies = []
	
	for x in ciphertext:
		frequencies.append({})
		frequency = frequencies[-1]
		for i in range(0, len(x)):
			if x[i] in frequency.keys():
				frequency[x[i]] += 1
			else:
				frequency[x[i]] = 1
	#print('Characters = {}\n Frequency = {}'.format(repr(ciphertext[1]), frequencies[1], end=''))
	print(frequency.values())

	total_characters = len(ciphertext)
	percentile = {}
	high_percentile = {}

	for i in frequency.keys():
		percentile[i] = (frequency[i] / float(total_characters)) * 100
		if percentile[i] > 1.0:
			high_percentile = percentile[i]
	print(high_percentile)


def brentxor(ciphertext, key):
	
	plaintext = ''
	for x in range(0, len(ciphertext)):
		for y in range(0, len(ciphertext[x])):
			for z in (ciphertext[y]):
				plaintext += (chr(ord(z)^ord(key)))	
	
	return plaintext

def main():
	
	#empty string buffer for file
	file_obj = ''

	with open('../files/4.txt') as f:
		for line in f:
			file_obj += line.strip() #strip because CRLF

	#decode hex
	a = file_obj.decode('hex')

	#make file_obj list, 60 char stings for each index
	cipherlist = map(''.join, zip(*[iter(a)]*60))	
	
	charfreq(cipherlist)
	#print(brentxor(cipherlist, 'x'))

if __name__ == '__main__':
	main()


#this prints list into dict
#alist = {i : cipherlist[i] for i in range(0, len(cipherlist))}

