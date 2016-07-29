from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'voter/(?P<person>[\w]+)', voter),
]
