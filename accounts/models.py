from django.db import models
from django.contrib.auth.models import User

# Create your models here.
INT_STUDENT = 1
INT_TEACHER = 2
INT_NOT_DEFINED = 3

class UserStatus(models.Model):
    STATUS_CHOICES = (
        (INT_STUDENT, 'student'),
        (INT_TEACHER, 'teacher'),
        (INT_NOT_DEFINED, 'Not Defined')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    user_status = models.CharField(choices=STATUS_CHOICES, default=1, max_length=1)

    def __str__(self):
        return "__user__" + self.user.username + "__status__" + str(self.user_status) + "__."
    
class UserEssentials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    user_email_verified = models.BooleanField(default=False)