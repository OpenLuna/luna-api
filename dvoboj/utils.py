import tweepy
from tweepy import OAuthHandler
from django.conf import settings
from tweepy import Stream
from tweepy.streaming import StreamListener
from .models import Twitt
import json

consumer_key = settings.TWITTER_CONSUMER_KEY
consumer_secret = settings.TWITTER_CONSUMER_SECRET
access_token = settings.TWITTER_OAUTH_TOKEN
access_secret = settings.TWITTER_OAUTH_SECRET
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

def get_tweeter_api():
	api = tweepy.API(auth)
	return api

from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
    	parsed = json.loads(data)
    	#Twitt(user=parsed["user"], url=data, content=data, timestamp=data,isVideo=data,isFoto=data, content_url=data)
        print data
        return True
 
    def on_error(self, status):
        print(status)
        return True

def setTwitterListener():
	twitter_stream = Stream(auth, MyListener(), timeout=60)
	twitter_stream.filter(track=['#dvoboj'])
	return twitter_stream
