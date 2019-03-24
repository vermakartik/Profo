from django.shortcuts import render, redirect
from Essentials.utils import userStatusDefined
from Student import forms
from accounts import models as accounts_models

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user_status_value = userStatusDefined(request.user)
        print("*-- Got user_status -> " + str(user_status_value))
        if user_status_value == False:
            return redirect('user:user_status')
        elif user_status_value == str(accounts_models.INT_STUDENT):
                return redirect('student:profile')
        elif user_status_value == str(accounts_models.INT_TEACHER):
                return redirect('teachers:profile') 
    return redirect('404_not_found')

def user_status_define(request):
    if request.method == 'POST':
        return redirect('user:user_profile_form', user_status=request.POST['user_status'])
    elif request.method == "GET":
        return render(request, 'Essentials/user_status.html')

def user_profile_form(request, user_status):
        print(user_status)
        if user_status == 'student':
                return redirect('student:profile_form')
        elif user_status == 'teacher':
                return redirect('teachers:profile_form')
                