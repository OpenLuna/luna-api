from django.shortcuts import render
import requests

# Create your views here.
def voter(request, person):

	if person == "oce":
		requests.get("http://dvoboj.si/api/voteForOce/polica")
	elif person == "sin":
		requests.get("http://dvoboj.si/api/voteForSin/polica")

	return render(request, 'voter/page.html', {})