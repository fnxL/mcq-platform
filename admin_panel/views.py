
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse 
from . import views
from tests.models import Test
from questions.models import Question
from tests.forms import QuestionForm, TestForm
from django.contrib import messages


@login_required(login_url="/login")
def admin_panel(request):

    if request.user.is_staff:
        return render(request,'admin/dashboard.html')


    return render(request,'pages/403.html')

@staff_member_required(login_url="/login")
def manage_practice(request):
    objs = Test.objects.all().filter(test_type=1)
 
    return render(request,'admin/manage.html', {'tests': objs})

@staff_member_required(login_url="/login")
def manage_grand(request):
    objs = Test.objects.all().filter(test_type=2)
 
    return render(request,'admin/manage.html', {'tests': objs})

@staff_member_required(login_url="/login")
def list_all_tests(request):
    objs = Test.objects.all()
    return render(request,'admin/manage.html', {'tests': objs})

@staff_member_required(login_url="/login")
def test_view(request, tid):
   
    test = Test.objects.get(id=tid)
    questions = test.questions.all()
    count = questions.count
    return render(request, 'admin/testview.html', {'questions': questions, 'tests':test, 'count':count})

@staff_member_required(login_url="/login")
def add_question(request, tid):
    
    if request.method == "POST":
        form = QuestionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            instance = form.save()
            test = Test.objects.get(id=tid)
            test.questions.add(instance)
            messages.success(request,"Question added!")
            return redirect(reverse('test_view',args=[tid]))   
        

    return render(request, 'admin/addquestion.html', {'tid':tid})

@staff_member_required(login_url="/login")
def delete_question(request, tid, quid):
    obj = Question.objects.get(id=quid)
    obj.delete()
    messages.error(request, "Question deleted!")
    return redirect(reverse('test_view', args=[tid]))

@staff_member_required(login_url="/login")
def delete_test(request, tid):
    boj = Test.objects.get(id=tid)
    boj.delete()
    messages.error(request, "Test deleted successfully!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    
@staff_member_required(login_url="/login")
def create_test(request):

    if request.method == "POST":
        form = TestForm(data=request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request,'Test Successfully Created!')
            
            return redirect(reverse('test_view', args=[instance.id]))

    return render(request, 'admin/createtest.html')