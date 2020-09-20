from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
import datetime

# Create your views here.

def create_event(request):
	form = EventForm(request.POST or None)
	print(form.data)
	if request.method == 'POST' and form.is_valid():
		subject = form.cleaned_data['subject']
		description = form.cleaned_data['description']
		start_time = form.cleaned_data['start_time']
		clock = form.cleaned_data['clock']

		minute = clock * 30
		end_time = start_time + datetime.timedelta(minutes = minute)
		
		Event.objects.get_or_create(
			subject = subject,
			description = description,
			start_time = start_time,
			clock = clock,
			end_time = end_time,

		)
		return redirect('weekschedule-home')
	
	form_error = True
	
	return render(request, 'weekschedule/weekschedule.html', {'form': form, 'form_error': form_error, })



