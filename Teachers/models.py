from django.db import models
from django.contrib.auth.models import User
from Department import models as dept_models

# Create your models here.
class Teacher(models.Model):
    teacher_first_name = models.CharField(max_length = 1024, default="", blank=False, null=False)
    teacher_last_name = models.CharField(max_length = 1024, default = "", blank = False, null = False)
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_email = models.CharField(max_length=1024, default = "", blank = True, null=True)
    teacher_branch = models.ForeignKey(dept_models.Department, on_delete=models.CASCADE)