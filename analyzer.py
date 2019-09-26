#!/usr/bin/python3.6

import tweepy
from tweepy import OAuthHandler
import re
import nltk 


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
if __name__ == "__main__" :
    print("Twitter Sentiment Analyzer\n")
    userAccount = api.user_timeline(id = '', count = 100, include_rts = False)
    allText = ''
    for status in userAccount :
        print(status.user.name + ' said...')
        print(status.text + '\n')
        allText += status.text

    # removing extra spaces
    allText = re.sub(r'\s+', ' ', allText)

    # removes all the special characters and digits (only letters)
    formatted_allText = re.sub('[^a-zA-Z]', ' ', allText)
    formatted_allText = re.sub(r'\s+', ' ', formatted_allText)

    # use formatted version to create weighted frequency 
  




