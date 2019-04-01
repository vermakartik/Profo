from django.db import models
from Teachers.models import Teacher
import datetime

# Create your models here.
class Test(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    test_name = models.CharField(max_length = 1024, default="", null= False, blank=False)
    is_published = models.BooleanField(default=False)
    available_time = models.TimeField(auto_now=False, default=datetime.time(0, 10, 0, 0))

    def __str__(self):
        return(self.test_name + "_" + str(self.available_time))

class Question(models.Model):
    question_text = models.CharField(max_length = 16563, default="", null=False, blank=False)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)

class Answer(models.Model):
    answer_text = models.CharField(max_length = 256, default = "", null = False, blank = False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_answer_correct = models.BooleanField()