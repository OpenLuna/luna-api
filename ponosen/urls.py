from django.conf.urls import url
from ponosen.views import *

urlpatterns = [
    url(r'^save_email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', saveEmail),
    url(r'^req_recover_password/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', reqRecoverPassword),
    url(r'^recover_password/(?P<code>[\w ]+)/', recoverPassword),
    url(r'^ping/', ping),
]
