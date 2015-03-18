#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python /var/www/intelllex/python/bigram.py

#sudo apt-get install python-dev; sudo pip install -U numpy; sudo pip install -U nltk
#python -m nltk.downloader stopwords; python -m nltk.downloader punkt; python -m nltk.downloader wordnet

"""
* @python name:		python/bigram.py
* @description:		This file reads "pin_henry" table and writes to "dress" table.
* @related issues:	ITL-002
* @author:			Don Hsieh
* @since:			03/18/2015
* @last modified:	03/18/2015
* @called by:
"""
# from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder

"""
* @def name:		getBigram()
* @description:		This function removes stop words from content, handles stemming,
*					 and writes to "tokens" column.
* @related issues:	ITL-002
* @param:			void
* @return:			void
* @author:			Don Hsieh
* @since:			03/18/2015
* @last modified:	03/18/2015
* @called by:		main
*					 in python/bigram.py
"""
def getBigram():
	table = 'tokens'
	fields = 'id, content'
	# where = '`url` = "' + url + '" LIMIT 1'
	where = None
	rows = don.queryDB(dbName, table, fields, where)
	# print rows
	print len(rows)
	for row in rows:
		id = row[0]
		content = row[1]

		words = don.tokenize(content)
		print words
		print len(words)
		# bcf = BigramCollocationFinder.from_words(words)
		# bcf.apply_word_filter(filter_stopwords)
		# bcf = BigramCollocationFinder.from_words(lst)
		# print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 10)
		# print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 50)
		# print bcf.nbest(BigramAssocMeasures.chi_sq, 50)

		# bigrams = don.getBigrams(words, 50)
		# print bigrams
		feature = don.getFeature(words, 50)
		print feature
		print len(feature)
		raise

		tokens = []
		for s in lst:
			if isinstance(s, (basestring, unicode)):
				s = s.strip(', _\t\n\r"()[]:/-.;`*')
				# if len(s) > 2 and '?' not in s and ')' not in s and '$' not in s:
				if len(s) > 2 and '?' not in s and ')' not in s and not don.isNumber(s):
					# s = snowball_stemmer.stem(s)
					# s = wordnet_lemmatizer.lemmatize(s)
					s = don.stemming(s)
					tokens.append(s)
		tokens = list(set(tokens))
		tokens.sort()
		tokens = ' '.join(tokens)
		tokens_len = len(tokens)

		fields = 'tokens, tokens_len, updatedAt'
		# args = (stop, token_len, don.getNow())
		lstArgs = [tokens, tokens_len, don.getNow()]
		where = '`id`="' + str(id) + '"'
		don.updateDB(dbName, table, fields, where, lstArgs)
		









import don


dbName = 'intelllex'
# getContent()
getBigram()

# nltk.download()
# raise

print "Done"