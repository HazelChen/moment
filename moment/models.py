#coding:utf-8
from django.db import models
from datetime import datetime

class Word(models.Model):
	room = models.CharField(max_length=30)
	word = models.CharField(max_length=1024)
	timestamp = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.word
		
