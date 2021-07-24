
 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Question, Test
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
            'image',
            'question_type',
            'marks',
            'negative_marks',
            'option1',
            'option1_image',
            'option2',
            'option2_image',
            'option3',
            'option3_image',
            'option4',
            'option4_image',
            'correct_answer',
            'correct_option'
        ]

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'name',
            'topics',
            'test_type',
            'number_of_question',
            'time_limit',
            'max_marks',
        ]