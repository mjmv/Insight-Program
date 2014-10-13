## This script calculates the sentiment score of JSON encoded Twitter API obtained tweets.  Sentiment scores for individual words uses the Afinn scoring system.

import sys
import json
import re


def lines(fp):
	str(len(fp.readlines()))
	fp.seek(0)

def main():
	tweet_file = open(sys.argv[1]) 
	sent_file = open(sys.argv[2])

	scores = {} 
	parsedTweets = []

	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
      		parsedTweets.append(json.loads(line.encode('utf-8')))

	for tweet in parsedTweets:
		tweets = tweet.get("text", "Z").encode('utf-8') #get each unique tweet.  
		words = re.sub('[!@:,#"$%&-?._();]','',tweets).lstrip().rstrip().lower().split() #scrub punctuation
      
		sentiment = 0

		for word in words:
			if word in scores:
				sentiment+= scores[word]
		print str(sentiment)
        


    


if __name__ == '__main__':
    main()
