from django.urls import path
from .views import EventPage, EventAJAX, TodayPage, UpdateClockStatusAJAX, EventDeleteAJAX

urlpatterns = [
    path('today/', TodayPage, name='weekschedule-today'),
    path('weekschedule/', EventPage, name='weekschedule-home'),
    path('weekschedule/calendarAJAX', EventAJAX, name='weekschedule-calendarAJAX'),
    path('today/clockAJAX', UpdateClockStatusAJAX, name='today-clockAJAX'),
    path('weekschedule/eventdeleteAJAX', EventDeleteAJAX, name='weekschedule-eventdeleteAJAX')
]
