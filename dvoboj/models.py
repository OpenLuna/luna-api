from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Points(models.Model):
	oce = models.IntegerField(default=0)
	sin = models.IntegerField(default=0)


class Twitt_media(models.Model):
	isVideo = models.BooleanField(default=False)
	isFoto = models.BooleanField(default=False)
	isURL = models.BooleanField(default=False)
	content_url = models.URLField(null=True, blank=True)
	display_url = models.URLField(null=True, blank=True)

	def media_type(self):
		if self.isFoto:
			return "foto"
		elif self.isVideo:
			return "video"
		else:
			return "unkown"

	def __str__(self):
		return self.content_url


class Twitt(models.Model):
	user = models.CharField(max_length=1024)
	twitt_id = models.CharField(max_length=64, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	content = models.CharField(max_length=256, null=True, blank=True)
	timestamp = models.DateTimeField()
	media_data = models.ManyToManyField(Twitt_media, blank=True)

	def __str__(self):
		return self.user
