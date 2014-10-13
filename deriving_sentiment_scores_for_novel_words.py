## Script: (1) extracts and parses tweets from JSON encoded Twitter API data; (2) calculates the sentiment for a tweet based on words present in AFINN-111.txt; (3) deposits words from tweet that are not included in the AFINN-111 sentiment score text in a dictionary, and initialized dictionary value as sentiment score for this first tweet word found in; (3) deposits each word into a list.  one list per tweet; (4) transfers words from tweet lists to dictionary, setting value as number of tweets a word was found in; (5) calculates and returns a derived sentiment score for Non-AFINN words by summing sentiment scores across all tweets that contained the given word and dividing by the number of tweets which contained the word.

import sys
import re
import json


   
def lines(fp):
	str(len(fp.readlines()))
	fp.seek(0)


def main():    
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	AFINN = {} #pre-calculated sentiment scores
	parsedTweets = [] #retains tweet order
	New_Sentiment = {} #to hold words from tweets absent in AFINN with value as sum of sentiments scores across all tweets containing given word
	Unique_Words = {} #to hold words from tweets absent in AFINN with value as count of tweets containing word 



	for line in sent_file:
		term, score  = line.split("\t")  #the file is tab-delimited. "\t" means "tab character"
		AFINN[term] = int(score)  #convert the score to an integer

	
	for line in tweet_file:
		parsedTweets.append(json.loads(line.encode('utf-8')))


	for tweet in parsedTweets:
		if 'lang' in tweet and tweet['lang'] == 'en': #remove non-English tweets 
			tweets = tweet.get("text", "").encode('utf-8') #get unique tweets.  had to re-encode it for some reason
			words = re.sub(r'[@!",:;#?]','',tweets).lower().split() #scrub punctuation	
			
			sentiment = 0	
			unique_words = [] #to hold words from tweets absent in AFINN
			
			
			for word in words:
				if word in AFINN:
					sentiment += AFINN[word] #get sent score for each tweet	
							
			for word in words:
				if word not in AFINN and word not in New_Sentiment:
					New_Sentiment[word] = sentiment #initialize value for novel words as AFINN sentiment score of text word was initially found in.
				elif word in New_Sentiment:
					New_Sentiment[word] = New_Sentiment[word] + sentiment #for each non-AFINN word, continue to add sentiment score for successive tweets containing word.    
			for word in words:
				if word not in AFINN and word not in unique_words:
					unique_words.append(word) #makes list of non-AFINN words from tweet
		

			for word in unique_words:
				Unique_Words[word] = Unique_Words.get(word,0) + 1 #transfer non-AFINN words to dictionary, w/ count of tweets containing word as value
	
			Derived_Sentiment = {k: float(New_Sentiment[k])/Unique_Words[k] for k in Unique_Words} #calculates a sentiment score for each non-AFINN as average sentiment of AFINN words from all tweets the non-AFINN word found in.  
		

	for word in Derived_Sentiment:
		print word, Derived_Sentiment[word] #prints a list containing non-AFINN words and corresponding derived sentiment score.



if __name__ == '__main__':
    main()
