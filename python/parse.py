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
* @def name:		getTypesOfNullContent()
* @description:		This function prints Distinct "application_type" of records whose "content" is null.
* @related issues:	ITL-001
* @param:			void
* @return:			void
* @author:			Don Hsieh
* @since:			03/04/2015
* @last modified:	03/04/2015
* @called by:		main
*					 in python/parse.py
"""
def getTypesOfNullContent():
	dbName = 'intelllex'
	table = 'document_dump'
	fields = 'DISTINCT application_type'
	where = '`content` = ""'
	# where = '`Available` = "Y" OR `Available` = "R" OR `Available` = "N"'
	rows = don.queryDB(dbName, table, fields, where)
	print rows
	print len(rows)
	# return args





"""
* @def name:		parseContent(s)
* @description:		This function parses data to gets url, application_type, and content.
* @related issues:	ITL-001
* @param:			string s
* @return:			tuple args
* @author:			Don Hsieh
* @since:			03/03/2015
* @last modified:	03/04/2015
* @called by:		main
*					 in python/parse.py
"""
def parseContent(s):
	args = None
	if 'Content::' in s:
		s = s.split('Content::')[-1]
		header = s.split('Content:')[0].split('\n')
		url = ''
		application_type = ''
		for line in header:
			if 'url: http' in line:
				url = line.split('url: ')[-1].strip(', _\t\n\r')
			elif 'contentType: ' in line:
				application_type = line.split('contentType: ')[-1].strip(', _\t\n\r')
		# print url
		# print application_type
		types = ['image/jpeg', 'image/png', 'application/msword', 'application/pdf']
		if application_type in types:
			content = ''
		else:
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
		dbName = 'intelllex'
		table = 'document_dump'
		fields = 'url, application_type, content'
		args = (url, application_type, content)
		# args = (url, application_type, content, now)
		# don.insertDB('intelllex', 'document_dump', fields, args)
		don.insertDB(dbName, table, fields, args)
	return args




import don

timeStart = don.getNow()
filepath = '/var/www/intelllex/data/dump'
# filepath = '/var/www/intelllex/data/dump2'
s = ''
insertions = []

fields = 'url, application_type, content'
lstLength = []
# for col in range(len(rows[0])):
for col in range(len(fields.split(', '))):
	lstLength.append(-1)

cntRows = 0
with open(filepath) as f:
	lines = f.readlines()
	key = 1
	for line in lines:
		# if key % 10000 == 0:
		# if key % 50000 == 0:
		if 'Recno:: ' in line:
			args = parseContent(s)
			if args is not None:
				cntRows += 1
				lstLength = don.getMaxLengthOfFields(args, lstLength)
			# if args is not None:
			# 	insertions.append(args)
			s = ''
		else: s += line
		# if key % 50000 == 0:
		# if key % 100000 == 0:
		# if key % 150000 == 0:
		if key % 250000 == 0:
		# if key % 1000000 == 0:
			now = don.getNow()
			print '\n' + now + '\t\t' + str(key) + ' / ' + str(len(lines)) + '\t\t' + '(' + str(round(100 * key / len(lines), 2)) + '%)'
			print 'Elapsed: ' + str(don.timeDiff(timeStart, now)) + '\t\t' + 'Statrt time: ' + timeStart + '\t\t' + str(cntRows) + ' insertions'
			# row = insertions[-1]
			# print type(row)
			print args[0]
			print args[1]
			# print args[0] + '\t\t\t' + args[1]
			# print row[0]
			# raise
		key += 1

args = parseContent(s)
lstLength = don.getMaxLengthOfFields(args, lstLength)
print lstLength
# insertions.append(args)
# don.getMaxLengthOfEachField(insertions)
l = [426, 25, 66724]	#dump2
l = [468, 73, 67662]	#dump
getTypesOfNullContent()

print '\n' + 'Statrt time: ' + timeStart + '\t\t' + 'Elapsed: ' + str(don.timeDiff(timeStart, now))
print "Done"