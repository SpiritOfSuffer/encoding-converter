#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import base64
from urllib2 import quote, unquote

filepath = 'C:\\Users\\Dom\\Desktop\\Projects\\netstalking\\data.txt' # Here put your path to the file with text(in default format, or in base64)

reload(sys)
sys.setdefaultencoding('utf-8') # Making an utf-8 coding

def encode_base64(filepath):
	data = read_file(filepath)
	encoded_data = base64.b64encode(data)
	write_file(filepath, encoded_data)
	print(encoded_data)

def decode_base64(filepath):
	data = read_file(filepath)
	decoded_data = base64.b64decode(data)
	write_file(filepath, decoded_data)
	print(decoded_data)

def decode_url(filepath):
	url = read_file(filepath)
	decoded_url = unquote(unquote(url))
	write_file(filepath, decoded_url)
	print(decoded_url)	

def encode_url(filepath):
	url = read_file(filepath)
	encoded_url = quote(quote(url))
	write_file(filepath, encoded_url)
	print(encoded_url)

#There are a subsidiary functions below

def read_file(filepath):
	with open(filepath) as r:
		data = r.read()
	return data 

def write_file(filepath, data):
	with open(filepath, 'w') as w:
		w.write(data)

#encode_url(filepath) Call this, if you want to encode to url format
#decode_url(filepath) Call this, if you want to decode from url format
#encode_base64(filepath) Call this, if you want to encode text in base64
#decode_base64(filepath) Call this, if you want to decode text from base64

#  This is a simple script for decode/encode text from/in base64
 
#  Created by Sublime Text 2.
#  Developer: Deuse
#  Date: 22.01.2017
#  Creation Time: 17:02
#  Last update: 22.01.2017 at 17:36
