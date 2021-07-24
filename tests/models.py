from django.db import models
from django.db.models.expressions import Value
from django.contrib.auth.models import User
from questions.models import Question


class Test(models.Model):
    name = models.CharField(max_length=150)
    topics = models.TextField(blank=True)
    test_type = models.IntegerField()
    number_of_question = models.IntegerField(default=0)
    time_limit = models.FloatField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    max_marks = models.IntegerField(default=0) 
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)