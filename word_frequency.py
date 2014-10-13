## This script extracts tweets from JSON encoded Twitter API output, and calculates the frequency of tweeted words.

import sys
import json
import re


def lines(fp):
	str(len(fp.readlines()))
	fp.seek(0)

def main():
	counts = {}
	freqs = {}

	tweet_file = open(sys.argv[1])

	parsedTweets = [] #want data to be in list so it retains order, per instructions

	for line in tweet_file:
		parsedTweets.append(json.loads(line.encode('utf-8')))

	for tweet in parsedTweets:
		tweets = tweet.get("text", " ").encode('utf-8') #get each unique tweet.  Had to re-encode it.
		scrub1 = re.sub('[!@:,#"$%&-?._();]','',tweets) #scrub punctuation
		scrub2 = scrub1.lstrip() #strip leading white space
		scrub3 = scrub2.rstrip() #strip trailing white space
		scrub4 = scrub3.lower()
		words = scrub4.split()
				
		for word in words:	
			if word not in counts:
				counts[word] = 1
			else:
				counts[word] += 1

	sum_counts = float(sum(counts.values())) #getting total number of words
	counts.update((x, float(y/sum_counts)) for x, y in counts.items()) #updating dic with frequency of words 	
	for word in counts: 
		print word, counts[word]


	

    



    

if __name__ == '__main__':
    main()
