from django.shortcuts import render
from collections import defaultdict

# Create your views here.
from datetime import datetime
from django.shortcuts import render
from .models import Link


def learning(request):
    roll = Link.objects.all()
    chart_data = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_data[l.subject].append(l.grade)
    Labels.append(u'English')
    
    for s, g in chart_data.items():
        print(s, g)
    # chart_data_string = ','.join(chart_data)
    # for i in  roll:
    #     Labels.append(i.scope)
    # str_Labels = '","'.join(Labels)


    
    str_Labels = str(Labels)
    # print(str_Labels)
    return render(request, 'learning.html', {
        'roll': roll,
        'chart_data': dict(chart_data),
        'str_Labels':str_Labels,
    })
#query = "SELECT * FROM foo WHERE bar IN (%s)" % ','.join('?' * len(params))
#cursor.execute(query, params)
