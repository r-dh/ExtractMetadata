# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:48:54 2019

Converts metadata from H.264 files to .json

@author: remy.dheygere
"""

import re
import json
import sys
import os.path

try:
	if os.path.isfile(sys.argv[1]):
		file = sys.argv[1]
except Exception as e:
	print("Script requires h264 file as argument.")
	sys.exit()
	
with open(file, 'rb') as f:            # rb read binary
    data = f.read()

result = re.findall(b'(?<=\xff\xff\xff\xff\xff)\{.+?(?=\x00\x00\x00\x01)', data)
result = [str(part)[2:-1] for part in result]       # trim the b'' around every string

print(len(result), "strings found!")

regularjson = "[" + ",\n".join(result) + "]"
prettyjson = json.loads(regularjson)

with open(os.path.splitext(file)[0] + '_output.json', 'w') as joutput:
    #joutput.write(regularjson)                     # compact, on one line
    joutput.write(json.dumps(prettyjson, indent=4))