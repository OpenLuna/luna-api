from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^getPoints/', getPoints),
    url(r'^getOcesPoints/', getOcesPoints),
    url(r'^getSinsPoints/', getSinsPoints),
    url(r'^voteForOce/', voteForOce),
    url(r'^voteForSin/', voteForSin),
    url(r'^addVotesForOce/(?P<points>\d+)/', addVotesForOce),
    url(r'^addVotesForSin/(?P<points>\d+)/', addVotesForSin),
]