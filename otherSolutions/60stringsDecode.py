#!/usr/bin/python

from __future__ import print_function
import string

def charfreq(ciphertext):

	frequency = {}
	for i in range(0, len(ciphertext)):
		if ciphertext[i] in frequency.keys():
			frequency[ciphertext[i]] += 1
		else:
			frequency[ciphertext[i]] = 1
	return(frequency)

def brentxor(ciphertext, key):
	
	plaintext = ''
	for x in range(0, len(ciphertext)):
		plaintext += (chr(ord(ciphertext[x])^ord(key)))	
	return plaintext

def main():
	
	# empty string buffer for file
	file_obj = ''

	with open('../files/4.txt') as f:
		for line in f:
			file_obj += line.strip() #strip because CRLF

	# decode hex
	a = file_obj.decode('hex')

	# make file_obj list, 60 char stings for each index
	# this prints list into dict
	# alist = {i : cipherlist[i] for i in range(0, len(cipherlist))}
	# below is python comphrension above but written in a loop for my understanding	
	cipherlist = []
	for i in range(0, len(a)):
		if i % 60 == 0:
			cipherlist.append(a[i])
		else:
			cipherlist[-1] = cipherlist[-1] + a[i]
		print('i = {}'.format(i))	

	# algorithm that does the thing here, all the hard work is done.
	for line in cipherlist:
		freq = charfreq(line) # get the dict for the freq analys
		maxfreqnum = 0
		maxfreqchar = ''
		for x in freq.keys():
			if freq[x] > maxfreqnum:
				maxfreqnum = freq[x]
				maxfreqchar = x
		# import pdb; pdb.set_trace()
		# plaintext xor key = ciphertext
		# ciphertext xor plaintext = key?
		key = (chr(ord(maxfreqchar) ^ ord(' ')))
		print('key: {} plaintext: {}'.format(key,(brentxor(line, key))))

if __name__ == '__main__':
	main()

'''
	frequencies = []
	
	for x in ciphertext:
		frequencies.append({})
		frequency = frequencies[-1]
		for i in range(0, len(x)):
			if x[i] in frequency.keys():
				frequency[x[i]] += 1
			else:
				frequency[x[i]] = 1
	print('ciphertext is {}'.format(type(ciphertext)))
	print('frequencies is {}'.format(type(frequencies)))
	print('frequency is {}'.format(type(frequency)))

	print('Characters = \n Frequency = {}'.format(frequencies, end=''))
	
	total_characters = len(ciphertext)
	percentile = {}
	high_percentile = {}

	for i in frequency.keys():
		percentile[i] = (frequency[i] / float(total_characters)) * 100
		if percentile[i] > 1.0:
			high_percentile = percentile[i]
	#print(high_percentile)
'''
