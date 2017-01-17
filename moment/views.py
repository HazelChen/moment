#coding:utf-8
from django.shortcuts import render
from moment.models import Word
from moment.models import Room
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import logging
import  json

logger = logging.getLogger('views')

def public(request):
	room_id = request.GET.get('room')
	if room_id == None:
		room_id = 'default'

	words = []
	try:
		room = Room.objects.get(identifition=room_id);
	except Room.DoesNotExist:
		room = None

	if room != None:
		words = room.word_set.all().order_by("-timestamp")

	return render(request, 'moment.html', {'word_list': words, 'room': room_id})

def add_word_public(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	word_input = body['word']
	room_input = body['room']

	try:
		room = Room.objects.get(identifition = room_input);
	except Room.DoesNotExist:
		room = None

	if room is None:
		room = Room(identifition = room_input, duration = 300)
		room.save()

	word = Word(room = room, word = word_input)
	word.save()
	room.word_set.add(word)
	return HttpResponse()