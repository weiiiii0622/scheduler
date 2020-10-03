from django.shortcuts import render, redirect
from .models import Quiz
# Create your views here.

def Home(request):
	subject = Quiz.objects.values('subject').distinct()

	return render(request, 'QuizBank/Quizhome.html', {'subject': subject})

def Subject(request, id):
	year = Quiz.objects.filter(subject = id).values('year').distinct()

	return render(request, 'QuizBank/Quizsubject.html', {'year': year, 'id': id})

def TestPage(request, id, year):
	
	return render(request, 'QuizBank/Quizexam.html', {})
