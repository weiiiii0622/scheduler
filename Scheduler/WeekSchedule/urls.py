from django.urls import path
from .views import EventPage, EventAJAX, TodayPage

urlpatterns = [
    path('today/', TodayPage, name='weekschedule-today'),
    path('weekschedule/', EventPage, name='weekschedule-home'),
    path('weekschedule/calendarAJAX', EventAJAX, name='weekschedule-calendarAJAX'),
]
