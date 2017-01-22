#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import base64

filepath = 'C:\\Users\\Name\\Desktop\\Projects\\data.txt' # Here put your path to the file with text(in default format, or in base64)

def encode_base64(filename):
	with open(filename) as r:
		data = r.read()
		encoded_data = base64.b64encode(data)
	with open(filename, 'w') as w:
		w.write(encoded_data)

def decode_base64(filename):
	with open(filename) as r:
		data = r.read()
		decoded_data = base64.b64decode(data)
	with open(filename, 'w') as w:
		w.write(decoded_data)


encode_base64(filepath) # Call this, if you want to encode text in base64
decode_base64(filepath) # Call this, if you want to decode text from base64

#  This is a simple script for decode/encode text from/in base64
 
#  Created by Sublime Text 2.
#  Developer: Deuse
#  Date: 22.01.2017
#  Creation Time: 17:02
#  Last update: 22.01.2017 at 17:36


