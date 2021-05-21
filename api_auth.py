import os
import tweepy
import dotenv
from dotenv import load_dotenv

load_dotenv()
# assign the values accordingly
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret =  os.getenv('CONSUMER_SECRET')
access_token =  os.getenv('ACCESS_TOKEN')
access_token_secret =  os.getenv('ACCESS_TOKEN_SECRET')

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)
