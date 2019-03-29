from . import models
from django.forms import ModelForm

class CustomProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', "")
        super(CustomProfileForm, self).__init__(*args, **kwargs)


class TeacherSummaryForm(CustomProfileForm):
    class Meta:
        model = models.Teacher
        exclude = ['teacher_user']

