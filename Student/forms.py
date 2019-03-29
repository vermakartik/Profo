from django.forms import ModelForm, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from Student import models

class CustomProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', "")
        super(CustomProfileForm, self).__init__(*args, **kwargs)

class StudentGeneralProfileModelForm(ModelForm):
    class Meta:
        model = models.StudentGeneralProfileModel
        fields = "__all__"

class StudentFamilyDetailsModelForm(ModelForm):
    class Meta:
        model = models.StudentFamilyDetailsModel
        fields = "__all__"

class StudentContactDetailsModelForm(ModelForm):
    class Meta:
        model = models.StudentContactDetailsModel
        fields = "__all__"

class StudentSummaryModelForm(CustomProfileForm):
    class Meta:
        model = models.StudentSummaryModel
        exclude = ('student_user',)
        widgets = {
            'student_dob': DateInput(attrs={'type': 'date'})
        }

