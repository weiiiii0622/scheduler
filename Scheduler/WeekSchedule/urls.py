from django.urls import path
from .views import EventPage, EventAJAX

urlpatterns = [
    path('weekschedule/', EventPage, name='weekschedule-home'),
    path('weekschedule/calendarAJAX', EventAJAX, name='weekschedule-calendarAJAX'),
]
