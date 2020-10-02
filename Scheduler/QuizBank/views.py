from django.shortcuts import render, redirect
from .models import Quiz
# Create your views here.

def Home(request):
	subject = Quiz.objects.values('subject').distinct()
	print(subject)
	return render(request, 'QuizBank/Quizhome.html', {'subject': subject})

def Subject(request, id):
	print(id)
	year = Quiz.objects.filter(subject = id).values('year').distinct()
	# year = [x[0]['year'] for x in year]
	# print(year)
	return render(request, 'QuizBank/Quizsubject.html', {'year': year})

def TestPage(request):

	return
