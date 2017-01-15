#coding:utf-8
from django.shortcuts import render
from moment.models import Word
from django.http import HttpResponse
import logging
import  json

logger = logging.getLogger('views')

def public(request):
	return render(request, 'moment.html', {'word_list': Word.objects.order_by('-timestamp'), 'mode': 'public'})

def add_word_public(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	word_input = body['word']
	word = Word(room = 'default', word = word_input)
	word.save()
	return HttpResponse()

private_word_list = ['private']

def private(request):
	return render(request, 'moment.html', {'word_list': private_word_list, 'mode': 'private'})

def add_word_private(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	word_input = body['word']
	private_word_list.append(word_input)
	return HttpResponse()