## This script extracts hashtagged words from JSON encoded Twitter API output and returns the top ten most frequently hashtagged words and their counts.

import sys
import json
from operator import itemgetter


def lines(fp):
	str(len(fp.readlines()))
	fp.seek(0)

def main():

	count = {}
	
	tweet_file = open(sys.argv[1])

	parsedTweets = [] #want data to be in list so it retains order, per instructions

	for line in tweet_file:
		if "hashtags" in line:
			parsedTweets.append(json.loads(line.encode('utf-8')))

	for tweet in parsedTweets:
		firstLayer = tweet.get('entities', 'z').get('hashtags', 'z')#returns a list containing dictionary
	
		for i in range(len(firstLayer)):
			secondLayer = i, firstLayer[i] #returns a tuple 
	
			for i in range(len(secondLayer)):
				thirdLayer = secondLayer[1] # returns a dictionary
			Tag = thirdLayer.get(u'text', "").encode('utf-8') #returns the hashtag words as strings
			tag = Tag.lower().split()
						
			for word in tag:
				count[word] = count.get(word,0) + 1

	top = sorted(count.iteritems(), key=itemgetter(1))
	top_10 = top[-10:]

	for k,v in top_10: print k,v

		
		



	
	
if __name__ == '__main__':
    main()
