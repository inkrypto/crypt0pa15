#!/usr/bin/python

# string to encrypt
message = 't5rr1Jrtt6Jn1qJunz'

key = 13

#set to 'encrypt' or 'decrypt'
mode = 'decrypt'

#possible symbols to use
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#message buffer
translated = ''

for symbol in message:
	if symbol in SYMBOLS:
		symbol_index = SYMBOLS.find(symbol)

		#encrypt or decrypt
		if mode == 'encrypt':
			translated_index = symbol_index + key
		elif mode == 'decrypt':
			translated_index = symbol_index - key

		#handle the wraparound
		if translated_index >= len(SYMBOLS):
			translated_index -= len(SYMBOLS)
		elif translated_index < 0:
			translated_index += len(SYMBOLS)

		translated += SYMBOLS[translated_index]
	else:
		#append the symbol without encrypting/decrypting
		translated += symbol

print(translated)
