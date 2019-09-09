#!/usr/bin/python3.6

import tweepy

from tweepy import OAuthHandler

consumer_key = '8y3U5ASNoOdwxReKKx4wMRCd0'
consumer_secret = 'JjZKkPGNjBNN8n2pNLBDiwg3DHNEjUFPefEvgMNywk6SD6peRh'
#access_token = ''
#access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
if __name__ == "__main__" :
	print("Twitter Sentiment Analyzer\n")

	public_tweets = api.search('Dogs', rpp = 20, show_user = True)

	for e in public_tweets :
		print(e)