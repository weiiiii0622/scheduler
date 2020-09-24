from django.urls import path
from .views import EventPage

urlpatterns = [
    path('weekschedule/', EventPage, name='weekschedule-home'),
]
