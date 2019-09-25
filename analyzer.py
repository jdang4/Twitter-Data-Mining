#!/usr/bin/python3.6

import tweepy
from tweepy import OAuthHandler
import re
import nltk 


consumer_key = '8y3U5ASNoOdwxReKKx4wMRCd0'
consumer_secret = 'JjZKkPGNjBNN8n2pNLBDiwg3DHNEjUFPefEvgMNywk6SD6peRh'
access_token = '3666714796-UPSfym7yThx6VHZYmY8NJjkkkTzUbdDJ9vuodcI'
access_secret = 'ZI6vumAZzDPzXISg0AcK73STaqc6vwUrV7lLqRzPRlrsj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
if __name__ == "__main__" :
    print("Twitter Sentiment Analyzer\n")
    userAccount = api.user_timeline(id = '@andylieou', count = 100, include_rts = False)
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
  




