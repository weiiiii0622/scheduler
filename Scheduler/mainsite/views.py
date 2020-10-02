from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.http import is_safe_url

# Create your views here.

def homepage(request):
    return render(request, 'mainsite/home.html')

def User_register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mainsite-home')

	else:
		form = UserRegistrationForm()
	return render(request, 'mainsite/register.html', {'form':form})

def User_login(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')

    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_:
                return redirect(next_)
            else:
                return redirect("/")
        else:
            print('error')

    return render(request, "mainsite/login.html", {'form':form})

def User_logout(request):
    logout(request)
    return redirect("/login/")

def Grades(request):
    return render(request,"Grades/grades.html")

