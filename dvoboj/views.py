from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Points, Twitt, Twitt_media, Vote, Banner_image
import json
import re
import random

# Create your views here.
def getPoints(request):
	obj = Points.objects.all()[0]
	return JsonResponse({"oce": obj.oce,"sin": obj.sin, "winner": "oce" if obj.oce > obj.sin else "sin" if obj.oce < obj.sin else "tie"})

def getOcesPoints(request):
	obj = Points.objects.all()[0]
	return HttpResponse(obj.oce)

def getSinsPoints(request):
	obj = Points.objects.all()[0]
	return HttpResponse(obj.sin)

def voteForOce(request, source="P"):
	obj = Points.objects.all()[0]
	obj.oce += 1
	obj.save()
	Vote(option=Vote.OCE, source=source).save()
	return HttpResponse("Added")

def voteForSin(request, source="P"):
	obj = Points.objects.all()[0]
	obj.sin += 1
	obj.save()
	Vote(option=Vote.SIN, source=source).save()
	return HttpResponse("Added")

def addVotesForSin(request, points, source="P"):
	obj = Points.objects.all()[0]
	obj.sin += int(points)
	obj.save()
	for i in range(int(points)):
		Vote(option=Vote.SIN, source=source).save()
	return HttpResponse("Added")

def addVotesForOce(request, points, source="P"):
	obj = Points.objects.all()[0]
	obj.oce += int(points)
	obj.save()
	for i in range(int(points)):
		Vote(option=Vote.OCE, source=source).save()
	return HttpResponse("Added")

def getTweets(request, by=0):
	count = Twitt.objects.all().count()
	return JsonResponse({"tweets":[{"id":tweet.id,
									"twitt_id":tweet.twitt_id,
									"url":tweet.url, 
									"user":tweet.user,
									"time":tweet.timestamp.isoformat(),
									"user_profile":"https://twitter.com/"+tweet.user,
									"text":fillUrls(tweet.content, list(tweet.media_data.filter(isURL=True))),
									"media":[{"url": media.content_url, "type":media.media_type()}for media in tweet.media_data.filter(isURL=False)],} for tweet in list(reversed(Twitt.objects.all().order_by("id")))],
						 "tweets_count": count,
						})

def fillUrls(text, urls):
	p = re.compile('https?:\/\/[\w.\/-_#]*')
	pUrl = p.finditer(text)
	lustUrlju = list(pUrl)
	if len(lustUrlju)>len(urls):
		for blindUrl in lustUrlju[len(urls):]:
			start, end = blindUrl.span()
			text = text[:start]+text[end:]
	for url, sUrl in reversed(zip(lustUrlju, urls)):
		start, end = url.span()
		repText = '<a href="'+sUrl.content_url+'">'+sUrl.display_url+'</a>'
		text = text[:start]+repText+text[end:]
	return text


def getRandomImage(request):
	banners = list(Banner_image.objects.all())
	image = random.choice(banners)
	return HttpResponse("http://localhost:8888/"+image.image.url)