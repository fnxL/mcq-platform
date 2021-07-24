from django.db import models
 

class Question(models.Model):

    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    question_type = models.IntegerField(default=0)
    marks = models.IntegerField(default=1)
    negative_marks = models.FloatField(blank=True, null=True)
    option1 = models.TextField(blank=True)
    option1_image = models.ImageField(blank=True, upload_to='images/options/')

    option2 = models.TextField(blank=True)
    option2_image = models.ImageField(blank=True, upload_to='images/options/')

    option3 = models.TextField(blank=True)
    option3_image = models.ImageField(blank=True, upload_to='images/options/')

    option4 = models.TextField(blank=True)
    option4_image = models.ImageField(blank=True, upload_to='images/options/')
 
    correct_answer = models.TextField(blank=True)
    correct_option = models.IntegerField(blank=True,null=True)
 
 
    def save(self, *args, **kwargs):
        if not self.negative_marks:
            if self.marks == 1:
                self.negative_marks = 0.33
            else:
                self.negative_marks = 0.66
        
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.text)





