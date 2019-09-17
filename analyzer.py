#!/usr/bin/python3.6

import tweepy

from tweepy import OAuthHandler

consumer_key = '<insert key>'
consumer_secret = '<insert secret>'
access_token = '<insert token>'
access_secret = '<insert secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
if __name__ == "__main__" :
	print("Twitter Sentiment Analyzer\n")

	for status in tweepy.Cursor(api.home_timeline).items(10) :
            print(status.text)
