from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return redirect('weekschedule-today')

def User_register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mainsite-login')

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
                return redirect('/today/')
        else:
            print('error')
            err = 'Password is wrong'
            return render(request, "mainsite/login.html", {'form':form, 'err': err})

    return render(request, "mainsite/login.html", {'form':form})

def User_logout(request):
    logout(request)
    return redirect("/login/")

@login_required
def Grades(request):
    return render(request,"Grades/grades.html")

