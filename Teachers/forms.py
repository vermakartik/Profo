from . import models
from django.forms import ModelForm

class TeacherSummaryForm(ModelForm):
    class Meta:
        model = models.Teacher
        exclude = ['teacher_user']

