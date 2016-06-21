from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Points(models.Model):
    oce = models.IntegerField(default=0)
    sin = models.IntegerField(default=0)


class Vote(models.Model):
    OCE = "O"
    SIN = "S"
    SHELF = "S"
    PAGE = "P"
    VOTE_OPTIONS = (
        (OCE, 'Oce'),
        (SIN, 'Sin'),
    )
    VOTE_SOURCE = (
        (SHELF, 'Shelf'),
        (PAGE, 'Page'),
    )

    date = models.DateTimeField(auto_now=True)
    option = models.CharField(max_length=1,
                              blank=True, null=True,
                              choices=VOTE_OPTIONS)
    source = models.CharField(max_length=64,
                              blank=True, null=True)
    def __str__(self):
        return self.option + " " + str(self.date) + " " + self.source


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
            return "unknown"

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
