from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.

def homepage(request):
    return render(request, 'mainsite/home.html')

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mainsite-home')

	else:
		form = UserRegistrationForm()
	return render(request, 'mainsite/register.html', {'form':form})
