from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PonosenEmail(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email

class RecoverPassword(models.Model):
	user = models.ForeignKey("PonosenEmail")
	code = models.CharField(max_length=32)

	def __str__(self):
		return self.code