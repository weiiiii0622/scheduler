from django.urls import path
from .views import create_event

urlpatterns = [
    path('weekschedule/', create_event, name='weekschedule-home'),
]
