from django.urls import path
from .views import Home, Subject, TestPage

urlpatterns = [
    path('QuizBank/', Home, name='quizbank-home'),
    path('QuizBank/<str:id>', Subject, name='quizbank-subject'),
    path('QuizBank/<str:id>/<str:year>', TestPage, name='quizbank-test'),
]