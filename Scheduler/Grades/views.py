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
        print("Normal")
        current_user = request.user
        options = current_user.get_grades_test_option()
        options.append(test_type)
        current_user.set_grades_test_option(options)
        current_user.save()
        
        return JsonResponse({},status=200)
    
    return JsonResponse({},status=400)


@login_required
def learning(request):
    roll = Link.objects.all()

    context = {}
    current_user = request.user
    options = current_user.get_grades_test_option()

    current_user = request.user
    #choices = current_user.get_grades_test_option()
    return render(request, 'Grades/grades.html',{
        'roll': roll,
        'context':context,
        'form':GradesChoicesForm([(v, v) for v in options]),
    })

@login_required
# def subject_ajax(request):
#     if request.is_ajax() and request.method == 'POST':
	    
#         return render(request,'Grades/grades.html')

#     return render(request,'Grades/grades.html')

def grades_to_subject(request,sub):
    data_subject = Link.objects.filter(subject=sub)
    test_link = Link.objects.filter(subject=sub).values_list('test',flat=True).distinct()
    current_user = request.user
    
    options = current_user.get_grades_test_option()

    return render(request,'Grades/grades_subject.html',{
        'data_subject':data_subject,
        'sub':sub,
        'form':GradesChoicesForm([(v, v) for v in options]),
        'test_link':test_link,
        })

@login_required 
def subject_to_test(request,sub,test):
    data_test = Link.objects.filter(subject=sub,test=test)
    chart_labels = list(Link.objects.filter(subject=sub,test=test).values_list('scope',flat=True))
    chart_datas =list (Link.objects.filter(subject=sub,test=test).values_list('grade',flat=True))
    test_link = Link.objects.filter(subject=sub).values_list('test',flat=True).distinct()
    str_test = str(test)

    current_user = request.user 
    options = current_user.get_grades_test_option()
        # for sub in roll:
        #     s = sub.subject
        #     for word in words:
        #     letter = word[0]
        #     bord_dict.setdefault(s, '').append(word)
    return render(request,'Grades/grades_test.html',{
        'data_test':data_test,
        'sub':sub,
        'test':test,
        'form':GradesChoicesForm([(v, v) for v in options]),
        'chart_labels':chart_labels,
        'chart_datas':chart_datas,
        'str_test':str_test,
        'test_link':test_link,
    })

def CreateGradeAJAX(request):
    if request.is_ajax():
        print("IminHEre")
        user = request.user
        subject = int(request.POST.get('subject'))
        test = request.POST.get('test')
        date = request.POST.get('date')
        scope = request.POST.get('scope')
        grade = request.POST.get('grade')

        print(user)

        Link.objects.get_or_create(
            user = user,
            subject = subject,
            test = test,
            scope = scope,
            grade = grade,
            date = date
        )

        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)

@login_required
def EventDeleteAJAX(request):
    if request.is_ajax():
        id = request.POST.get('id')
        print(id)
        target_event = Link.objects.get(id = id)
        print(target_event)
        target_event.delete()
    return JsonResponse({}, status=200)
