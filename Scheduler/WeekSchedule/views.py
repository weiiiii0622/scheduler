from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

# Create your views here.

def create_event(request):
	form = EventForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		subject = form.cleaned_data['subject']
		description = form.cleaned_data['description']
		start_time = form.cleaned_data['start_time']
		clock = form.cleaned_data['clock']

		Event.objects.get_or_create(
			subject = subject,
			description = description,
			start_time = start_time,
			clock = clock,
		)
		return redirect('weekschedule-home')
	
	return render(request, 'weekschedule/weekschedule.html', {'form':form})



