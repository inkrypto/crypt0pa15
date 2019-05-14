#!/usr/bin/python

import random, sys, string, math, transModule, decryptModule

def main():
	
	random.seed(42)

	for i in range(20):
		
		#gen message of random len
		message = string.ascii_uppercase * random.randint(4, 40)

		#convert message to list and shuffle it
		message = list(message)
		random.shuffle(message)
		message = ''.join(message)

		print('Test "#%s: %s..."' % (i + 1, message[:50]))

		#check for all possible keys for each message
		for key in range(1, len(message)/2):
			encrypted = transModule.encrypt_message(key, message)
			decrypted = decryptModule.decrypt_message(key, encrypted)

			#if don't match
			if message != decrypted:
				print('Mismatch with key %s and message %s.' % (key, message))
				print('Decyrpted as: ' + decrypted)
				sys.exiti()

	print('Transition cipher test passed')

if __name__ == '__main__': main()
