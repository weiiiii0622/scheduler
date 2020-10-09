from collections import defaultdict
from datetime import datetime
from django.shortcuts import render ,redirect
from .models import Link

from django.contrib.auth.decorators import login_required

from .forms import LinkModelForm ,GradesChoicesForm
from mainsite.models import User
from django.http import JsonResponse
import json


@login_required
def form_choices(request):
    context = {}
    current_user = request.user
    
    options = current_user.get_grades_test_option()
    context['form'] = GradesChoicesForm([(v, v) for v in options])
    
    return render(request,'Grades/grades.html',context)

@login_required
def GradesAJAX(request):

    if request.is_ajax() and request.method == 'POST':
        test_type = request.POST.get('test_type')

        current_user = request.user
        options = current_user.get_grades_test_option()
        options.append(test_type)
        current_user.set_grades_test_option(options)
        current_user.save()
        
        return JsonResponse({})
    return render(request,'Grades/grades.html')


@login_required
def learning(request):
    roll = Link.objects.all()
    chart_subject = defaultdict(list)
    chart_scope = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        chart_scope[l.subject].append(l.scope)
        Labels.append(l.scope)

    context = {}
    current_user = request.user
    options = current_user.get_grades_test_option()

    user = User.objects.filter(account=request.user)
    str_Labels = str(Labels)
    current_user = request.user
    choices = current_user.get_grades_test_option()
    return render(request, 'Grades/grades.html',{
        'roll': roll,
        'chart_subject': dict(chart_subject),
        'user':user,
        'choices':choices,
        'chart_scope':dict(chart_scope),
        'str_Labels': str_Labels,
        'context':context,
        'form':GradesChoicesForm([(v, v) for v in options]),
    })

@login_required
# def subject_ajax(request):
#     if request.is_ajax() and request.method == 'POST':
	    
#         return render(request,'Grades/grades.html')

#     return render(request,'Grades/grades.html')

def grades_to_subject(request,subject):
    data_subject = Link.objects.filter(subject=subject)
    roll = Link.objects.all()
    chart_subject = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        Labels.append(l.scope)
        

    return render(request,'Grades/grades_subject.html',{
        'data_subject':data_subject,
        'roll':roll,
        'chart_subject':dict(chart_subject),
        'str_Labels':str_Labels,
        })

@login_required 
def subject_to_test(request,subject,test):
    data_test = Link.objects.filter(subject=subject,test=test)
    

        # for sub in roll:
        #     s = sub.subject
        #     for word in words:
        #     letter = word[0]
        #     bord_dict.setdefault(s, '').append(word)
    return render(request,'Grades/grades_test.html',{
        'data_test':data_test,
    })
