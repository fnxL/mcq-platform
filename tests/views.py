from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse 
from .forms import CreateUserForm, QuestionForm, TestForm
from django.contrib.auth.decorators import login_required
from .models import Test,Status
from results.models import Result, TestStatus
from questions.models import Question
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
 
# Create your views here.
# User Client
def home(request):
    last5 = Test.objects.all().order_by('-id')[:6]
 
    return  render(request, 'pages/home.html' , {'last5': last5})


def details(request, qid):
    obj = Test.objects.get(id=qid)
   
    return render(request, 'pages/cmodal.html' , {'obj': obj})

def log_out(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome Back, {}".format(user.first_name))
            return redirect('home')
        else:
            pass
        #handle error

    return render(request, 'pages/login.html') 


def register(request):
    
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created. Please login.")
            return redirect('login')

        ##eror handling.
    
    context =  {'form': form}
    return render(request, 'pages/register.html', context)


def view_tests(request,test_type:str):
    temp = 0
    if test_type=="practice":
        temp = 1
    else:
        temp = 2

    tests = Test.objects.filter(test_type=temp)
    return render(request, 'pages/view_tests.html', {'tests': tests})

 

@login_required(login_url='login')
def start_test(request,tid):

    user = request.user
    test = Test.objects.get(pk=tid)
    time_limit = test.time_limit * 60.0
    
    context = {
        "test": test,
        "question_list":test.questions.all(),
        "mins": time_limit
    }
 

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        time_taken = request.POST['time_taken']
        test = request.POST['test_obj']
        test_obj = Test.objects.get(name=test)
        question_list = test_obj.questions.all()
        score = 0
        total_attempted = 0
        negative_marks = 0
        
        correct_marks = 0
        correct_question = 0
        incorrect_question = 0
        questions_left = 0
        correct_list = []
        data = []
        for ques in question_list:
            user_ans_list = []
            user_nat_ans = ""
            user_ans = request.POST.get(ques.text, False)
            if not user_ans:
                questions_left += 1
            else:
                total_attempted += 1
                correct = False
                if ques.question_type == 3:
                    user_ans = request.POST.get(ques.text, False)
                    user_nat_ans = user_ans
                    if (ques.correct_answer == user_ans):
                        correct = True
                        correct_question += 1
                        score += ques.marks
                        correct_marks += ques.marks
                    else:
                        correct = False
                        incorrect_question += 1
                    
                elif ques.question_type == 2:
                    user_ans_list = request.POST.getlist(ques.text)
                    user_ans = ''.join(str(i) for i in user_ans_list)
                    user_ans_list = [int(i) for i in user_ans_list]
                    correct_list = [int(x) for x in str(ques.correct_option)]
                    print(correct_list)
                    if (ques.correct_option == int(user_ans)):
                        correct = True
                        correct_question += 1
                        score += ques.marks
                        correct_marks += ques.marks
                    else:
                        correct = False
                        incorrect_question += 1
                else:
                    user_ans = int(request.POST.get(ques.text, False))
                    if(ques.correct_option == user_ans):
                        correct = True
                        correct_question += 1
                        score += ques.marks
                        correct_marks += ques.marks
                    else:
                        correct = False
                        score -= ques.negative_marks
                        negative_marks += ques.negative_marks
                        incorrect_question += 1

    
                temp = {
                    'choice': user_ans,
                    'correct': correct,
                    'choice_list': user_ans_list,
                    'correct_list': correct_list,
                    'user_ans': user_nat_ans
                }
                data.append(temp)
                
 
        total_marks = score
        result_data = Result()
        result_data.test = test_obj
        result_data.user = user
        result_data.total_attempted = total_attempted
        result_data.questions_left = questions_left
        result_data.incorrect_questions = incorrect_question
        result_data.total_time_taken = time_taken
        result_data.correct_questions = correct_question
        result_data.correct_marks = correct_marks
        result_data.negative_marks = round(negative_marks,2)
        result_data.total_marks = round(total_marks,2)
        result_data.data = data
        result_data.save()
        status, notcreated = TestStatus.objects.get_or_create(test=test_obj,user=request.user)
        return redirect(reverse('report', args=[test_obj.id,result_data.id]))

         
            


    return render(request, 'pages/start_test.html', context)


 