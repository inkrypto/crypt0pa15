#!/usr/bin/python

import sys

def main():


	my_message = "this is a test message!"
	my_key = 4 

	ciphertext = encrypt_message(my_key, my_message)

	#print encrypted with pipe in case their are spaces at the end, formatting.
	print(ciphertext + "|")

def encrypt_message(key, message):
	#each string represents a column
	ciphertext = [''] * key

	#loop through each column in ciphertext
	for column in range(key):
		current_index = column

		#continue loop until current_index goes past message length
		while current_index < len(message):
			#put char at current_index in message at then of the current column in the ciphertext list
			ciphertext[column] += message[current_index]

			#move current_index over:
			current_index += key

	#convert ciphertext list into single string
	return ''.join(ciphertext)

if __name__ == '__main__': main()


