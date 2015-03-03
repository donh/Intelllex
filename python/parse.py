#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python /var/www/intelllex/python/parse.py

"""
* @python name:		python/parse.py
* @description:		This file reads "pin_henry" table and writes to "dress" table.
* @related issues:	ITL-001
* @author:			Don Hsieh
* @since:			03/03/2015
* @last modified:	03/03/2015
* @called by:
"""


import re

"""
* @def name:		insertDB(dbName, table, fields, args)
* @description:		This function inserts data into database.
* @related issues:	ITL-001
* @param:			string s
* @return:			tuple args
* @author:			Don Hsieh
* @since:			03/03/2015
* @last modified:	03/03/2015
* @called by:		main
*					 in python/parse.py
"""
def parseContent(s):
	args = None
	if 'Content::' in s:
		s = s.split('Content::')[-1]
		header = s.split('Content:')[0].split('\n')
		# body = s.split('Content:')[-1].lstrip()
		body = s.split('Content:')[-1].lstrip().decode('ascii', 'ignore')
		body = s.split('Content:')[-1]
		body = re.sub('\t+', ' ', body)
		body = re.sub(' +', ' ', body)
		body = re.sub('\n+', '\n', body)
		content = body.strip(', _\t\n\r')
		# content.decode('utf-8')
		# content = content.decode('ascii')
		# content = content.decode('ascii', 'ignore')
		# anchorText = anchorText.decode('ascii', 'ignore')
		# content = s.split('Content:')[-1].lstrip()

		url = ''
		application_type = ''
		for line in header:
			if 'url: http' in line:
				url = line.split('url: ')[-1]
			elif 'contentType: ' in line:
				application_type = line.split('contentType: ')[-1]
		# print url
		# print application_type

		dbName = 'intelllex'
		table = 'document_dump'
		fields = 'url, application_type, content'
		args = (url, application_type, content)
		# args = (url, application_type, content, now)
		# don.insertDB('intelllex', 'document_dump', fields, args)
		don.insertDB(dbName, table, fields, args)
	return args




import don
filepath = '/var/www/intelllex/data/dump'
# filepath = '/var/www/intelllex/data/dump2'
s = ''
insertions = []
with open(filepath) as f:
	lines = f.readlines()
	key = 1
	for line in lines:
		# if key % 10000 == 0:
		# if key % 50000 == 0:
		if 'Recno:: ' in line:
			args = parseContent(s)
			# if args is not None:
			# 	insertions.append(args)
			s = ''
		else: s += line
		if key % 100000 == 0:
		# if key % 1000000 == 0:
			print str(key) + ' / ' + str(len(lines)) + '\t\t' + '(' + str(round(100 * key / len(lines))) + '%)'
			# row = insertions[-1]
			# print type(row)
			print args[0] + '\t\t\t' + args[1]
			# print row[0]
			# raise
		key += 1

args = parseContent(s)
# insertions.append(args)
# don.getMaxLengthOfEachField(insertions)
l = [426, 25, 66724]

print "Done"