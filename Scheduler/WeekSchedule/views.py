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
			print("HIi")
			return JsonResponse({}, status = 200)

	return render(request, 'weekschedule/weekschedule.html', {'form': form,})
	
def EventAJAX(request):

	if request.is_ajax() and request.method == 'GET':
		year = int(request.GET.get('year'))
		month = int(request.GET.get('month'))
		date = int(request.GET.get('date'))

		target_date = datetime.datetime(year, month, date)
		target = Event.objects.filter(start_time__contains = target_date.date())
		
		print(target)
		target_event = {
			'subject': target[0].subject,
			'description': target[0].description,
			'start_time':target[0].start_time,
			'end_time': target[0].end_time,
			'status': target[0].status,
		}

		data = {
			'target_event': target_event,
		}

	return JsonResponse(data, status = 200)






