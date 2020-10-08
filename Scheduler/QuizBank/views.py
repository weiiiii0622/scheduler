from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Quiz

import random

# Create your views here.
question = ['question1', 'question2', 'question3']
image = ['image1', 'image2', 'image3']
answer = ['option1', 'option2', 'option3', 'option4', 'option5', 'option6', 'option7', 'option8', 'option9', 'option10', 'option11', 'option12', 'option13' , 'option14', 'option15']
number = []

@login_required
def Home(request):
	subject = Quiz.objects.values('subject').distinct()

	return render(request, 'QuizBank/Quizhome.html', {'subject': subject})

@login_required
def Subject(request, id):
	year = Quiz.objects.filter(subject = id).values('year').distinct()

	return render(request, 'QuizBank/Quizsubject.html', {'year': year, 'id': id})

@login_required
def TestPage(request, id, year):

	if request.is_ajax():
		number.append(request.GET.get('number'))
		return JsonResponse({}, status = 200)	
	
	random_box = Quiz.objects.filter(subject= id, year= year).values_list('id', flat=True)

	try:
		if number[0] == 'all' or int(number[0]) > len(random_box):
			pass
		elif number[0] == '10':
			random_box = random.sample(list(random_box), 10)
		elif number[0] == '20':
			random_box = random.sample(list(random_box), 20)
		elif number[0] == '30':
			random_box = random.sample(list(random_box), 30)
	except:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	quiz = Quiz.objects.filter(id__in = random_box)
	
	id_data = []
	question_data = {}
	image_data = {}
	option_data = {}
	
	for x in quiz:

		id_data.append(x.id)
		question_fields = [getattr(x, field) for field in question if getattr(x, field) is not None and getattr(x, field) is not '']
		image_fields = [getattr(x, field) for field in image if getattr(x, field) is not None and getattr(x, field) is not '']
		option_fields = [getattr(x, field) for field in answer if getattr(x, field) is not None and getattr(x, field) is not '']
		question_data[x.id] = question_fields
		image_data[x.id] = image_fields
		option_data[x.id]= option_fields

	data = {
		'id': id_data,
		'question': question_data,
		'image': image_data,
		'option': option_data,
		'subject': id,
	}
	number.clear()
	
	return render(request, 'QuizBank/Quizexam.html', data)

@login_required
def CheckAnswerAJAX(request, id, year):
	if request.is_ajax():
		answers = []
		id_list = request.GET.getlist('id')
		print(id_list)
		quiz = Quiz.objects.filter(id__in = id_list)
		
		for quiz in quiz:
			for answer in quiz.answer.split(","):
				answers.append("{id}-{answer}".format(id=quiz.id, answer=answer))

		print(answers)

		return JsonResponse({'answer': answers}, status = 200)