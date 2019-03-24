from django.contrib import admin

# Register your models here.
from Student.models import StudentContactDetailsModel, StudentFamilyDetailsModel, StudentGeneralProfileModel, StudentSummaryModel, StudentTestModel

admin.site.register(StudentContactDetailsModel)
admin.site.register(StudentFamilyDetailsModel)
admin.site.register(StudentGeneralProfileModel)
admin.site.register(StudentSummaryModel)
admin.site.register(StudentTestModel)