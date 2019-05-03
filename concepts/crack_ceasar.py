#!/usr/bin/python

# string to encrypt
message = 't5rr1Jrtt6Jn1qJunz'

#possible symbols to use
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#loop through all possible keys
for key in range(len(SYMBOLS)):
	translated = ''

	#loop through each symbol in message
	for symbol in message:
		if symbol in SYMBOLS:
			symbol_index = SYMBOLS.find(symbol)
			
			#append decrypted symbol
			translated_index = symbol_index - key

			#handle the wraparound
			if translated_index < 0:
				translated_index += len(SYMBOLS)
			
			#append raw symbol
			translated += SYMBOLS[translated_index]

		
		else:
			#append the symbol without encrypting/decrypting
			translated += symbol

	print('Key #%s: %s' % (key, translated))
