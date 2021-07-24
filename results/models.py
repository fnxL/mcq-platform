import questions
from django.db import models
from tests.models import Test
from django.contrib.auth.models import User

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_attempted = models.IntegerField()
    questions_left = models.IntegerField()
    #corr marks
    #neg marks
    #------
    data = models.TextField(blank=True)

    correct_questions = models.IntegerField()
    incorrect_questions =  models.IntegerField()
    total_time_taken = models.IntegerField() # seconds
    #final score
    correct_marks = models.FloatField() #done
    negative_marks = models.FloatField() #dfone
    total_marks = models.FloatField() #done

    def __str__(self) -> str:
        return str(self.pk)

class TestStatus(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.pk)
    
    class Meta:
        verbose_name_plural = "TestStatus"
 

