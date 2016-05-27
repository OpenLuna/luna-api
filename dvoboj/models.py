from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Points(models.Model):
	oce = models.IntegerField(default=0)
	sin = models.IntegerField(default=0)

class Twitt(models.Model):
	user = models.CharField(max_length=1024)
	url = models.URLField(null=True, blank=True)
	content = models.CharField(max_length=256, null=True, blank=True)
	timestamp = models.DateTimeField()
	isVideo = models.BooleanField(default=False)
	isFoto = models.BooleanField(default=False)
	content_url = models.URLField(null=True, blank=True)