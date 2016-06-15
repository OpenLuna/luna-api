import tweepy
from tweepy import OAuthHandler
from django.conf import settings
from tweepy import Stream
from tweepy.streaming import StreamListener
from .models import Twitt, Twitt_media
import json
from datetime import datetime, timedelta
from django.db import connection
import requests

consumer_key = settings.TWITTER_CONSUMER_KEY
consumer_secret = settings.TWITTER_CONSUMER_SECRET
access_token = settings.TWITTER_OAUTH_TOKEN
access_secret = settings.TWITTER_OAUTH_SECRET
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

def get_tweeter_api():
	api = tweepy.API(auth)
	return api

 
class MyListener(StreamListener):
 
    def on_data(self, data):
	connection.close()
        print data
    	data = json.loads(data)
        isFoto = False
        isVideo = False
        media_url = None
        url = "https://twitter.com/"+data["user"]["screen_name"]+"/status/"+data["id_str"]
        time = datetime.strptime(data["created_at"],"%a %b %d %H:%M:%S +0000 %Y") + timedelta(hours=2)
        tweet = Twitt(user=data["user"]["screen_name"], twitt_id=data["id_str"], url=url, content=data["text"], timestamp=time)
        tweet.save()

        if "media" in data["entities"].keys():
            if data["extended_entities"]["media"][0]["type"] in ["photo", "animated_gif"]:
                isFoto=True
                media_url = data["extended_entities"]["media"][0]["media_url_https"]
            elif data["extended_entities"]["media"][0]["type"]=="video":
                isVideo=True
                media_url = data["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"]
            media=Twitt_media(isFoto=isFoto, isVideo=isVideo, content_url=media_url)
            media.save()
            tweet.media_data.add(media)
        if "urls" in data["entities"].keys():
            for url_in in data["entities"]["urls"]:
                media=Twitt_media(isURL=True, content_url=url_in["url"], display_url=url_in["display_url"])
                media.save()
                tweet.media_data.add(media)

        print data
        return True
 
    def on_error(self, status):
        print(status)
        return True

def setTwitterListener():
    while True:
        try:
            twitter_stream = Stream(auth, MyListener(), timeout=60)
            twitter_stream.filter(track=['#dvoboj'])
        except Exception, e:
            print "Error. Restarting Stream.... Error: "
            print e.__doc__
            print e.message


def removeRemovedTwitts():
    for twitt in Twitt.objects.all():
        if requests.get(twitt.url).status_code == 404:
            twitt.delete()
