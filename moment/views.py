#coding:utf-8
from django.shortcuts import render
from moment.models import Word
from django.http import HttpResponse
import logging
import  json

logger = logging.getLogger('views')

def index(request):
	return render(request, 'moment.html', {'word_list': Word.objects.all()})

def add_word(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	logger.info('json decoded')
	word_input = body['word']
	logger.info(word_input)
	word = Word(room = 'default', word = word_input)
	logger.info('build word')
	word.save()
	logger.info('save word')
	return HttpResponse()