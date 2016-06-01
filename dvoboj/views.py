from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Points, Twitt
import json
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
	return JsonResponse([{"id":tweet.id, "url":tweet.url, "user":tweet.user} for tweet in Twitt.objects.all().order_by("-id")[int(by):int(by)+10]], safe=False)