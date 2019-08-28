#!/urs/bin/python

import string

english_freq = {'e': 11.16, 'a': 8.49, 'r': 7.58, 'i':7.54, 'o':7.16, 't':6.95, 'n':6.65, 's':5.73, 'l':5.48, 'c': 4.53, 'u':3.63, 'd':3.38, 'p':3.16, 'm':3.01 , 'h':3.00, 'g':2.47, 'b':2.07, 'f':1.81, 'y':1.77, 'w':1.28, 'k':1.10, 'v':1.00, 'x':0.29, 'z':0.27, 'j':0.19, 'q':0.19}

def main():
	
	ciphertext = ''
	with open('../files/4.txt') as f:
		for line in f:
			ciphertext += line.strip().decode('hex')

	x = ''
	for i in range(0, 255):
		key = chr(i)
		for j in ciphertext:
			x += chr(ord(j)^ord(key))	
	
	print(x)
if __name__ == '__main__': main()
