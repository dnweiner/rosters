### the purpose of this file is to compare the email rosters of STL and APO with that of SoFoHo 2 (2016-2017) ###
### to see if any of my residents are tour guides or fellow members ###

import sys, os, csv, re

#####
#following code co-opted from CSE330S wiki to check for command line arguments
if len(sys.argv) < 4:
	sys.exit("Usage: %s filename" % sys.argv[0])

stl = sys.argv[1]
apo = sys.argv[2]
sofoho = sys.argv[3]

if not os.path.exists(stl):
	sys.exit("Error: File '%s' not found" % sys.argv[1])
	
if not os.path.exists(apo):
	sys.exit("Error: File '%s' not found" % sys.argv[2])
	
if not os.path.exists(sofoho):
	sys.exit("Error: File '%s' not found" % sys.argv[3])
	

#####

wustlkey_pattern = re.compile(r".*@") #check for everything before '@'

guide_wustlkeys = [] #initialize empty guides list
member_wustlkeys = [] #initialize empty members list
resident_wustlkeys = [] #initialize empty residents list

with open(stl, "r") as stl_file:
	for line in stl_file:
		r_wustlkey = re.search(wustlkey_pattern, line)
		wustlkey = r_wustlkey.group()
		wustlkey = wustlkey[:(len(wustlkey)-1)] # cut off the @
		guide_wustlkeys.append(wustlkey) # fill guides list
# print guide_wustlkeys

with open(apo, "r") as apo_file:
	for line in apo_file:
		r_wustlkey = re.search(wustlkey_pattern, line)
		if r_wustlkey is not None:
			wustlkey = r_wustlkey.group()
			wustlkey = wustlkey[:(len(wustlkey)-1)] # cut off the @
			member_wustlkeys.append(wustlkey) # fill residents list
# print member_wustlkeys

with open(sofoho, "r") as sofoho_file:
	for line in sofoho_file:
		r_wustlkey = re.search(wustlkey_pattern, line)
		if r_wustlkey is not None:
			wustlkey = r_wustlkey.group()
			wustlkey = wustlkey[:(len(wustlkey)-1)] # cut off the @
			if wustlkey == 'dnweiner': continue # no need to tell me which activities I'm in...
			resident_wustlkeys.append(wustlkey) # fill residents list
# print resident_wustlkeys

print "Residents who are tour guides: " + str(set(guide_wustlkeys).intersection(set(resident_wustlkeys)))[5:-2]
print "=========="
print "Residents who are in APO: " + str(set(member_wustlkeys).intersection(set(resident_wustlkeys)))[5:-2]
# print "=========="
# print "Tour guides who are in APO: " + str(set(guide_wustlkeys).intersection(set(member_wustlkeys)))[5:-2]