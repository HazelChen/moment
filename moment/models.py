#coding:utf-8
from django.db import models
from datetime import datetime

class Room(models.Model):
	identifition = models.CharField(max_length=32, primary_key=True, unique=True)
	duration = models.IntegerField()

	def __str__(self):
		return self.identifition


class Word(models.Model):
	room = models.ForeignKey(Room, default='default')
	word = models.CharField(max_length=1024)
	timestamp = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.word
		
