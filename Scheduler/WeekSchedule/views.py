from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.http import JsonResponse

import datetime


# Create your views here.


	
	
def EventPage(request):
	form = EventForm()

	if request.is_ajax():
		
		form = EventForm(request.POST)

		if form.is_valid():
			print(form)
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

			data = {
				'event': NewEvent,
			}
			
			return JsonResponse(data, status = 400)
		
		else:
			return JsonResponse({}, status=200)

	return render(request, 'weekschedule/weekschedule.html', {'form': form,})
	







