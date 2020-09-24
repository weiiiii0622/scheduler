from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import EventForm
from .models import Event

import datetime

# Create your views here.

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
			return JsonResponse({}, status = 400)

	return render(request, 'weekschedule/weekschedule.html', {'form': form,})
	







