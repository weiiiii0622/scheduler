from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Event

import datetime

# Create your views here.
@login_required
def EventPage(request):
	form = EventForm()

	if request.is_ajax():	
		form = EventForm(request.POST)

		if form.is_valid():

			subject = form.cleaned_data['subject']
			description = form.cleaned_data['description']
			start_time = form.cleaned_data['start_time']
			clock = form.cleaned_data['clock']
			minute = clock * 30
			end_time = start_time + datetime.timedelta(minutes = minute)
			NewEvent = Event.objects.get_or_create(
				user = request.user,
				subject = subject,
				description = description,
				start_time = start_time,
				clock = clock,
				end_time = end_time,
			)

			event = {
				'subject': NewEvent[0].subject,
				'description': NewEvent[0].description,
				'start_time': NewEvent[0].start_time,
				'clock': NewEvent[0].clock,
				'end_time': NewEvent[0].end_time,
			}

			data = {
				'event': event,
			}
			
			return JsonResponse(data, status = 200)	
		else:

			data = {
				'errors' : form.errors
			}
			print(form.errors.keys())
			return JsonResponse(data, status = 400)

	return render(request, 'WeekSchedule/weekschedule.html', {'form': form,})

@login_required
def EventAJAX(request):

	if request.is_ajax() and request.method == 'GET':
		year = int(request.GET.get('year'))
		month = int(request.GET.get('month'))
		date = int(request.GET.get('date'))

		target_user = get_user(request)
		target_date = datetime.datetime(year, month, date)
		print(target_date.date(), target_user)
		targets = Event.objects.filter(user = target_user, start_time__contains = target_date.date()).order_by('start_time')

		data = {
			'targets': serializers.serialize("json", targets),
		}

		if list(targets) == []:
			return JsonResponse(data, status = 400)
		else:
			return JsonResponse(data, status = 200)


@login_required
def TodayPage(request):
	today = datetime.datetime.now()
	target_user = get_user(request)
	
	events = Event.objects.filter(user = target_user, start_time__contains = today.date()).exclude(status = "Done")

	return render(request, 'WeekSchedule/today.html', {'events': events, })


@login_required
def UpdateClockStatusAJAX(request):
	if request.is_ajax() and request.method == 'GET':
		target_event_id = int(request.GET.get('target_event_id'))
		status = str(request.GET.get('status'))
		target_event = Event.objects.filter(id = target_event_id)

		target_event.update(status = status)

		return JsonResponse({}, status = 200)

@login_required
def EventDeleteAJAX(request):
	if request.is_ajax():
		id = request.GET.get('id')
		target_event = Event.objects.filter(id = id)
		target_event.delete()
	return JsonResponse({}, status=200)