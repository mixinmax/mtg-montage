#!/usr/bin/python

import sys
import argparse
import re
import os
import fnmatch

parser = argparse.ArgumentParser(prog='mtg-montage', description='Process images for print')
parser.add_argument('-d', '--directory', default='./', help='the directory where the card images are located')
parser.add_argument('-i', '--input', default='', required=True, help='input file with card names and quatity')
parser.add_argument('-o', '--output', default='', required=True, help='output pdf file to store the montage')
args = parser.parse_args()

matches = []
unmatched = []

input_lines = [line.strip() for line in open(args.input)]

for line in input_lines:

	# make sure the line in the file is correctly formatted
	line = re.search('^(\d+)\s+(.*)', line)
	if line != None:
		line = line.groups()
		if len(line) == 2:

			# find images in directory which match the name of the card
			pre_matches = []
			for root, dirnames, filenames in os.walk(args.directory):
				for filename in fnmatch.filter(filenames, line[1]+'*'):
					pre_matches.append(os.path.join(root, filename))

			if len(pre_matches) == 0:
				unmatched.append(line[1])
				print 'Couldn\'t find a match for', line[1]
			else:
				print 'Matched', line[1]
				# if there are more than one match, the user has to choose
				choice = 0
				if len(pre_matches) > 1:
					print 'Found more than one match for', line[1]
					for i, val in enumerate(pre_matches):
						print '  ' + repr(i) + '. ' + val
					choice = raw_input('  Which file would you like to use? (enter the number): ')
					choice = int(choice)
				
				# add the match from pre_matches to the main match list a number of times
				for _ in range(int(line[0])):
					matches.append(pre_matches[choice])

# build the montage command based on the images in matches[]
command = 'montage '
for img in matches:
	command = command + '"' + img + '" '
command = command + '-geometry 744x1039 -density 300 -tile 3x3 '
command = command + args.output

print ''
print 'Building the pdf. This may take a while...'
os.system(command)

print ''
print 'Statistics'
print '-------------------------------------------'
print '  Total different cards input:', len(input_lines)
print '  Total unsuccessful finds:', len(unmatched)
for sad in unmatched:
	print '    ', sad
print ''
