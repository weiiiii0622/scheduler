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
	form = EventForm(request.user, request.POST)

	if request.is_ajax():	
		# form = EventForm(request.POST)

		if form.is_valid():

			subject = form.cleaned_data['subject']
			description = form.cleaned_data['description']
			start_time = form.cleaned_data['start_time']
			clock = form.cleaned_data['clock']

			
			for i in range(clock):
				end_time = start_time + datetime.timedelta(minutes = 30)
				Event.objects.get_or_create(
					user = request.user,
					subject = subject,
					description = description,
					start_time = start_time,
					clock = clock,
					end_time = end_time,
				)
				start_time = start_time + datetime.timedelta(minutes = 30)

			
			return JsonResponse({}, status = 200)	
		else:

			data = {
				'errors' : form.errors
			}
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
	
	events = Event.objects.filter(user = target_user, start_time__contains = today.date()).exclude(status = "Done").order_by('start_time')

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