from django.forms import ModelForm, DateInput
from Student import models

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

class StudentSummaryModelForm(ModelForm):
    class Meta:
        model = models.StudentSummaryModel
        exclude = ('student_user',)
        widgets = {
            'student_dob': DateInput(format=('%d-%m-%Y'))
        }

