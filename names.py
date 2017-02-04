### the purpose of this file is to reformat roster names from "last, first" in one cell ###
### to "first" in one cell, "last" in another ###

import sys, os, csv, re, string

#####
#following code taken from CSE330 wiki to check for command line arguments
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])
#####
 
pattern = re.compile(r'(\w*)(, )(\w*)')

newlines = []

with open(filename, 'r') as f:
	for line in f:
		# print line
		email = line.split(',')[0].replace('email.','')
		match = re.search(pattern, line)
		if match is not None:
			last = match.group(1) # first group is the last name
			comma = match.group(2) # second group is the comma-space
			first = match.group(3) # third group is the first name
			newlines.append(email + "," + first + "," + last)
# print newlines

with open(filename, 'w') as new_f:
	for newline in newlines:
		new_f.write(newline + "\n")

### following code used to create a second file, rather than overwrite the original ###
# new_filename = filename[:-4] + "_fixed.csv"
# with open(new_filename, 'w') as new_f:
# 	for newline in newlines:
# 		new_f.write(newline + "\n")	