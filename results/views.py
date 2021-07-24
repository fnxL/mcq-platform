from django.shortcuts import render
from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse 
from tests.models import *
from questions.models import *
from .models import Result, TestStatus
from datetime import time, timedelta
import datetime
from ast import literal_eval

def result(request):
    test_status = TestStatus.objects.filter(user=request.user)
 
    return render(request, 'pages/results.html', {"tests": test_status})

def result_page(request, tid):

    result = Result.objects.filter(user=request.user,test=tid)
    print(result)
 
    return render(request, 'pages/results_page.html', {'results': result, 'name': result[0].test.name})

def report(request, tid, rid):
    result = Result.objects.get(id=rid);
    time = str(datetime.timedelta(seconds=result.total_time_taken))
    questions = result.test.questions.all()
    x = result.data
    data = literal_eval(x)
    
    final = list(zip(list(questions), list(data)))
    for i,j in final:
        print(i.option1, j)
    
    return render(request, 'pages/report.html', {'result': result, 'questions':questions,'time':time,'data':final})
