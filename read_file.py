"""
    Simple script to use dictionary file that parser created to be used in python script
    Loads dictionary with json and then allows it to be used in python 
"""

import json
import re

output_file = open("output_file.txt", "r")
#linije = count_file.readLines()
print("daj liniju:")
input = input()

for line in output_file:
	if(line.startswith(str(input) + ":")):
		result = line.find(":")
		dict = line[result+1:]
		print(dict)
		dict = str(dict).replace("'", "\"")
		print("popravljeni dict sa double quotavima:" + dict)
		dict = json.loads(dict)
		print("ovo je pravi dictionary: ")
		print(dict)
		for x,y in dict.items():
			print(x, y)

output_file.close()
