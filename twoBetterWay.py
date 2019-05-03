#!/usr/bin/python3

import sys

def xor_byte_strings(input_bytes1, input_bytes2):
	
	#initialize byte string to hold value of the XOR
	xord_bytes = b''

	#iterate through each char in each byte string
	for b1, b2 in zip(input_bytes1, input_bytes2):
		
		#XORs the byte and adds it to the byte string
		xord_bytes += (bytes([b1 ^ b2]))
		print(xord_bytes)
	return xord_bytes
	
def main():
	if len(sys.argv) != 3:
		print('Usage: ./two.py string1 string2')
		sys.exit(1)

	byte_string1 = bytes.fromhex(sys.argv[1])
	byte_string2 = bytes.fromhex(sys.argv[2])

	print(xor_byte_strings(byte_string1, byte_string2).hex())

if __name__ == '__main__':
	main()
