from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Points, Twitt, Twitt_media
import json
import re
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

def voteForOce(request):
	obj = Points.objects.all()[0]
	obj.oce += 1
	obj.save()
	return HttpResponse("Added")

def voteForSin(request):
	obj = Points.objects.all()[0]
	obj.sin += 1
	obj.save()
	return HttpResponse("Added")

def addVotesForSin(request, points):
	obj = Points.objects.all()[0]
	obj.sin += int(points)
	obj.save()
	return HttpResponse("Added")

def addVotesForOce(request, points):
	obj = Points.objects.all()[0]
	obj.oce += int(points)
	obj.save()
	return HttpResponse("Added")

def getTweets(request, by=0):
	print by
	count = Twitt.objects.all().count()
	return JsonResponse({"tweets":[{"id":tweet.id,
									"twitt_id":tweet.twitt_id,
									"url":tweet.url, 
									"user":tweet.user,
									"time":tweet.timestamp.isoformat(),
									"user_profile":"https://twitter.com/"+tweet.user,
									"text":fillUrls(tweet.content, list(tweet.media_data.filter(isURL=True))),
									"media":[{"url": media.content_url, "type":media.media_type()}for media in tweet.media_data.filter(isURL=False)],} for tweet in reversed(Twitt.objects.all().order_by("id")[int(by):int(by)+10])],
						 "tweets_count": count,
						})

def fillUrls(text, urls):
	p = re.compile('https?:\/\/[\w.\/-_#]*')
	pUrl = p.finditer(text)
	for url, sUrl in reversed(zip(pUrl, urls)):
		start, end = url.span()
		repText = '<a href="'+sUrl.content_url+'">'+sUrl.display_url+'</a>'
		text = text[:start]+repText+text[end:]
	return text
