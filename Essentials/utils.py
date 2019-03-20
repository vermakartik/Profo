from accounts.models import UserStatus
from accounts import models
from django.contrib.auth.models import User

def userStatusDefined(user):
    print("**--\[\e[02m\]User status Undefined Called--**")
    print(user)
    user = User.objects.get(username=user)
    userStatus = models.UserStatus.objects.get(user = user)
    print(userStatus.user_status)
    print(models.INT_NOT_DEFINED)
    
    if userStatus.user_status == str(models.INT_NOT_DEFINED):
        print('False returning...')
        return False
    else:
        print('false not returning...')
        return userStatus.user_status