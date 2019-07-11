#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
print('fhand is of type: {}'.format(type(fhand))) #print out the type so you know what datastructure your are working with
soup = BeautifulSoup(fhand, 'html.parser')
print('soup is of type: {}'.format(type(soup)))
tags = soup('span')
print('tags are of type: {}'.format(type(tags)))

# this is your algorithm. everything so far has been to get you the data. this is your algorithm to deal with that data
total = 0	#good work here. total had to be outside of main loop
for tag in tags:
	str_tag = str(tag)
	numbers = re.findall("[0-9]+", str_tag) #the re.findall converts the strings back into a list
	print('numbers are of type: {}'.format(type(numbers)))
	for number in numbers:
		str_number = int(number)	#name the variables close to what they are using letters gets confusing
		total += str_number
print(total)	#good work B!!
