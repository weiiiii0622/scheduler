from django.urls import path
from .views import EventPage, EventAJAX, TodayPage, UpdateClockStatusAJAX

urlpatterns = [
    path('today/', TodayPage, name='weekschedule-today'),
    path('weekschedule/', EventPage, name='weekschedule-home'),
    path('weekschedule/calendarAJAX', EventAJAX, name='weekschedule-calendarAJAX'),
    path('today/clockAJAX', UpdateClockStatusAJAX, name='today-clockAJAX'),
]
