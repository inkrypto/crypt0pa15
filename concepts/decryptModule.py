#!/usr/bin/python
import sys
import math

def main():
		
	my_message = "F  cuybhcoi!kut"
	my_key = 4 

	plaintext = decrypt_message(my_key, my_message)

	print(plaintext + "|")

def decrypt_message(key, message):

	#the number of columns
	num_columns = int(math.ceil(len(message)/float(key)))
	#the number of rows
	num_rows = key
	#the number of pads
	pads = (num_columns * num_rows) - len(message)

	#each string in plaintext represents a column
	plaintext = [''] * num_columns

	#column and row point to where the next char will go
	column = 0
	row = 0
	
	for symbol in message:
		plaintext[column] += symbol
		column += 1

		#if there are no more columns or at a shaded box, go to next row 1st column
		if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - pads):
			column = 0
			row += 1
	
	return ''.join(plaintext)

if __name__ == '__main__': main()


