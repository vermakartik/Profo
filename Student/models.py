from django.db import models
from django.core.validators import MaxValueValidator, MaxLengthValidator, MinLengthValidator
from Essentials.models import CategoryCasteModel
from django.contrib.auth.models import User
from CTest.models import Test, Question, Answer

# Create your models here.

MAX_LENGTH_SINGLE = 256
DEFAULT_STRING = ""
DEFAULT_INT = 0

class StudentGeneralProfileModel(models.Model):
    pass

class StudentFamilyDetailsModel(models.Model):
    pass
    
class StudentContactDetailsModel(models.Model):
    pass

class StudentSummaryModel(models.Model):
    CASTE_CATEGORY = (
        ('GEN', 'General or Open'),
        ('OBC', 'Other backward classes'),
        ('SC', 'Scheduled Caste'),
        ('ST', 'Scheduled Tribe'),
    )
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentRollNumber = models.CharField(max_length=MAX_LENGTH_SINGLE, null=False, blank=False, primary_key=True)
    # studentGeneralDetails = models.OneToOneField(StudentGeneralProfileModel, on_delete=models.CASCADE)
    # studentFamilyDetails = models.OneToOneField(StudentFamilyDetailsModel, on_delete=models.CASCADE)
    # studentContactDetails = models.OneToOneField(StudentContactDetailsModel, on_delete=models.CASCADE)

    student_first_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)
    student_last_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)
    student_dob = models.DateField(auto_now=False, null=False, blank=False)
    student_gender = models.CharField(max_length=MAX_LENGTH_SINGLE, blank=False, null=False)
    student_caste = models.CharField(choices=CASTE_CATEGORY, max_length=3, default='GEN')

    student_father_first_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)
    student_father_last_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)
    student_mother_first_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)
    student_mother_last_name = models.CharField(max_length=MAX_LENGTH_SINGLE, default=DEFAULT_STRING, null=False, blank=False)

    student_mobile = models.CharField(max_length=10, validators=[MaxLengthValidator(10), MinLengthValidator(10)], default=DEFAULT_INT, null=False, blank=False)
    student_emergency_contact = models.CharField(max_length=10, validators=[MaxLengthValidator(10), MinLengthValidator(10)], default=DEFAULT_INT, null=False, blank=False)
    student_phone_contact = models.CharField(max_length=10, null=True, blank=True)

INT_NOT_PERMITTED = 1
INT_REQUESTED = 2
INT_PERMITTED = 3

INT_ATTEMPTED = 4
INT_NOT_ATTEMPTED = 5
INT_DISQUALIFIED = 6

class QuestionResponse(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentSummaryModel, on_delete=models.CASCADE)

class StudentTestModel(models.Model):
    PERMISSION_STATUS = (
        (INT_NOT_PERMITTED, 'not-permitted'),
        (INT_REQUESTED, 'requested'),
        (INT_PERMITTED, 'permitted'),
    )

    ATTEMPT_STATUS = (
        (INT_ATTEMPTED, 'attempted'),
        (INT_DISQUALIFIED, 'disqualified'),
        (INT_NOT_ATTEMPTED, 'not-attempted'),
    )

    student_id = models.ForeignKey(StudentSummaryModel, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    student_score = models.IntegerField(default=-1)
    is_permitted = models.CharField(max_length=2, choices = PERMISSION_STATUS, default=INT_REQUESTED, null=False, blank = False)
    attempt_status = models.CharField(choices=ATTEMPT_STATUS, max_length=2, default = INT_NOT_ATTEMPTED, null = False, blank = False)

    class Meta:
        unique_together = ('student_id', 'test_id')