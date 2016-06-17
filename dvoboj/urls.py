from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^getPoints/', getPoints),
    url(r'^getOcesPoints/', getOcesPoints),
    url(r'^getSinsPoints/', getSinsPoints),

    url(r'^voteForOce/(?P<source>[\w]+)/', voteForOce),
    url(r'^voteForSin/(?P<source>[\w]+)/', voteForSin),
    url(r'^addVotesForOce/(?P<points>\d+)/(?P<source>[\w]+)/', addVotesForOce),
    url(r'^addVotesForSin/(?P<points>\d+)/(?P<source>[\w]+)/', addVotesForSin),

    url(r'^voteForOce/$', voteForOce),
    url(r'^voteForSin/$', voteForSin),
    url(r'^addVotesForOce/(?P<points>\d+)/$', addVotesForOce),
    url(r'^addVotesForSin/(?P<points>\d+)/$', addVotesForSin),

    url(r'^getTweets/(?P<by>\d+)/', getTweets),
    url(r'^getTweets/$', getTweets),
]
