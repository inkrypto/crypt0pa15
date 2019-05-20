#!/usr/bin/python

import os, time, sys, encryptModule, decryptModule

def main():
	
	frank = 'frank.encrypted.txt'
	out_file = 'babba'

	my_key = 10
	mode = 'decrypt' 

	#if no input file, terminate
	if not os.path.exists(frank):
		print('the file %s doesnt exist . . . ' % (frank))
		sys.exit(1)

	#if file exists, give user a chance to quit
	'''
	if os.path.exists(out_file):
		print('this file will overwrite %s. (C)ontinue or (Q)uit?' % (out_file))
		response =  raw_input('> ')
		if not response.lower().startswith('c'):
			sys.exit()
	'''
	#read the message from input file
	file_obj = open(frank)
	content = file_obj.read()
	file_obj.close()

	print('%sing . . .' % (mode.title()))

	#measure time
	start_time = time.time()
	if mode == 'encrypt':
		translated = encryptModule.encrypt_message(my_key, content)
	elif mode == 'decrypt':
		translated = decryptModule.decrypt_message(my_key, content)
	total_time = round(time.time() - start_time, 2)
	print('%sion time: %s seconds' % (mode.title(), total_time))

	#write translated message to file
	out_fileobj = open(out_file, 'w')
	out_fileobj.write(translated)
	out_fileobj.close()

	print('Done %sing %s (%s characters).' % (mode, frank, len(content)))
	print('%sed file is %s.' % (mode.title(), out_file))

if __name__ == '__main__': main()
