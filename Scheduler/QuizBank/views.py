from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Quiz

import random

# Create your views here.
question = ['question1', 'question2', 'question3']
image = ['image1', 'image2', 'image3']
answer = ['option1', 'option2', 'option3', 'option4', 'option5', 'option6', 'option7', 'option8', 'option9', 'option10', 'option11', 'option12', 'option13' , 'option14', 'option15']

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
		request.user.quiz_option = request.GET.get('number')
		request.user.save()
		return JsonResponse({}, status = 200)	
	
	random_box = Quiz.objects.filter(subject= id, year= year).values_list('id', flat=True)

	try:
		option = request.user.quiz_option
		if option == 'all' or int(option) > len(random_box):
			pass
		elif option == '10':
			random_box = random.sample(list(random_box), 10)
		elif option == '20':
			random_box = random.sample(list(random_box), 20)
		elif option == '30':
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
		'alert' : "作答時左右滑動來切換題目！",
	}
	messages.info(request, '作答時左右滑動來切換題目！')
	return render(request, 'QuizBank/Quizexam.html', data)

@login_required
def CheckAnswerAJAX(request, id, year):
	if request.is_ajax():
		answers = []
		id_list = request.GET.getlist('id')
		quiz = Quiz.objects.filter(id__in = id_list)
		
		for quiz in quiz:
			for answer in quiz.answer.split(","):
				answers.append("{id}-{answer}".format(id=quiz.id, answer=answer))

		

		return JsonResponse({'answer': answers}, status = 200)