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
    chart_subject = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        Labels.append(l.scope)

    context = {}
    current_user = request.user
    options = current_user.get_grades_test_option()
    str_Labels = str(Labels)
    current_user = request.user
    #choices = current_user.get_grades_test_option()
    return render(request, 'Grades/grades.html',{
        'roll': roll,
        'chart_subject': dict(chart_subject),
        'str_Labels': str_Labels,
        'context':context,
        'form':GradesChoicesForm([(v, v) for v in options]),
    })

@login_required
# def subject_ajax(request):
#     if request.is_ajax() and request.method == 'POST':
	    
#         return render(request,'Grades/grades.html')

#     return render(request,'Grades/grades.html')

def grades_to_subject(request,sub):
<<<<<<< HEAD
    data_subject = Link.objects.filter(subject=sub)
    test_link = Link.objects.filter(subject=sub).values_list('test',flat=True).distinct()
    current_user = request.user
=======
    data_subject = Link.objects.filter(user=request.user, subject=sub).values('test').distinct()
    current_user = request.user
    choices = current_user.get_grades_test_option()
    print("Hi", data_subject)
>>>>>>> 5c5caed576ddada0f990ab2eb905b7fcfa0514a4
    chart_subject = defaultdict(list)
    roll = Link.objects.all()
    
    options = current_user.get_grades_test_option()
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        #chart_scope[l.subject].append(l.scope)
        Labels.append(l.scope)
    str_Labels = str(Labels)
    return render(request,'Grades/grades_subject.html',{
        'data_subject':data_subject,
        'str_Labels':str_Labels,
        'sub':sub,
        'chart_subject':dict(chart_subject),
        'form':GradesChoicesForm([(v, v) for v in options]),
        'test_link':test_link,
        })

@login_required 
def subject_to_test(request,sub,test):
<<<<<<< HEAD
    data_test = Link.objects.filter(subject=sub,test=test)
    chart_labels = list(Link.objects.filter(subject=sub,test=test).values_list('scope',flat=True))
    chart_datas =list (Link.objects.filter(subject=sub,test=test).values_list('grade',flat=True))
=======
    data_test = Link.objects.filter(user=request.user, subject=sub,test=test)
>>>>>>> 5c5caed576ddada0f990ab2eb905b7fcfa0514a4
    roll = Link.objects.all()
    chart_subject = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        #chart_scope[l.subject].append(l.scope)
        Labels.append(l.scope)
    str_Labels = str(Labels)

    str_test = str(test)
    print(str_test)

    current_user = request.user 
    options = current_user.get_grades_test_option()
        # for sub in roll:
        #     s = sub.subject
        #     for word in words:
        #     letter = word[0]
        #     bord_dict.setdefault(s, '').append(word)
    return render(request,'Grades/grades_test.html',{
        'data_test':data_test,
        'str_Labels':str_Labels,
        'chart_subject':chart_subject,
        'test':test,
        'form':GradesChoicesForm([(v, v) for v in options]),
        'chart_labels':chart_labels,
        'chart_datas':chart_datas,
        'str_test':str_test,
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
		id = request.GET.get('id')
		target_event = Link.objects.filter(id = id)
		target_event.delete()
	return JsonResponse({}, status=200)
