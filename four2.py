#!/usr/bin/python

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
	for i in range(0, len(ciphertext)):
		plaintext += (chr(ord(ciphertext[i]) ^ ord(key)))	
	
	return plaintext

def main():
	
	# empty string buffer for file
	file_obj = ''

	with open('files/4.txt') as f:
		for line in f:
			file_obj += line.strip() #strip because CRLF

	# decode hex
	a = file_obj.decode('hex')

	# make file_obj a list, 60 char stings for each index
	# this prints list into dict
	# alist = {i : cipherlist[i] for i in range(0, len(cipherlist))}
	# below is the list comphrension from line above but written in a loop for my understanding	
	cipherlist = []
	for i in range(0, len(a)):
		if i % 60 == 0:					
			cipherlist.append(a[i])
		else:
			cipherlist[-1] = cipherlist[-1] + a[i]
	
	# algorithm that takes each line in list, runs frequency, counts max char and times used then xor max char  with 'assumed' plaintext char as the key
	# A xor B = C
	# B xor C = A
	# A xor C = B
	for line in cipherlist:
		freq = charfreq(line) # get the dict for the freq analys
		maxfreqnum = 0
		maxfreqchar = ''
		for i in freq.keys():
			if freq[i] > maxfreqnum:
				maxfreqnum = freq[i]
				maxfreqchar = i
		#import pdb; pdb.set_trace()
		# cheated here cause maxfreq char is '\x08' not space!!!
		key = chr(ord(maxfreqchar) ^ ord(' '))
		
		# line as ciphertext
		print('key={} \n plaintext={}'.format(repr(key), brentxor(line, key)))

if __name__ == '__main__':
	main()
