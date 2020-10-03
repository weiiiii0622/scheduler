from collections import defaultdict
from datetime import datetime
from django.shortcuts import render ,redirect
from .models import Link
from .forms import LinkModelForm ,GradesChoicesForm
from mainsite.models import User
from django.http import JsonResponse
import json


# def create(request):
#     form = LinkModelForm()
#     if request.method == "POST":
#         form = LinkModelForm(request.POST or None)
#         if form.is_valid():

#             date = form.cleaned_data['date']
#             test = form.cleaned_data['test']
#             scope = form.cleaned_data['scope']
#             grade = form.cleaned_data['grade']

#             form.save()
#             Link.objects.get_or_create(
#                 date = date,
#                 test = test,
#                 scope = scope,
#                 grade = grade,
#             )
#         return redirect("/Grades")
#     context = {
#         'form': form
#     }
#     return render(request, 'Grades/grades_form.html', context)
#{'form':form}

def form_choices(request):
    context = {}
    context['form'] = GradesChoicesForm(())
    choice_form = GradesChoicesForm(())
    # if request.method == "POST":
    #     form = LinkModelForm(request.POST or None)
    #     if form.is_valid():

    #         date = form.cleaned_data['date']
    #         test = form.cleaned_data['test']
    #         scope = form.cleaned_data['scope']
    #         grade = form.cleaned_data['grade']

    #         #form.save()
    #         Link.objects.get_or_create(
    #             date = date,
    #             test = test,
    #             scope = scope,
    #             grade = grade,8
    #         )
    #     return redirect("/Grades")  
    return render(request,'Grades/grades_form.html',context)



def GradesAJAX(request):
    
	if request.is_ajax() and request.method == 'POST':
		test_type = request.POST.get('test_type')
		
		return JsonResponse({})
	current_user = request.user
	user = User.objects.filter(account=current_user)
	user.update(grades_test_option=JsonResponse(test_type))
	return render(request,'Grades/grades_form.html')

def learning(request):
    roll = Link.objects.all()
    chart_subject = defaultdict(list)
    chart_test = defaultdict(list)
    chart_scope = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        chart_scope[l.subject].append(l.test)
        chart_scope[l.subject].append(l.scope)
        Labels.append(l.test)
    
    str_Labels = str(Labels)
    return render(request, 'Grades/grades.html',{
        'roll': roll,
        'chart_subject': dict(chart_subject),
        'chart_test':dict(chart_test),
        'cjart_scope':dict(chart_scope),
        'str_Labels': str_Labels,
    })


