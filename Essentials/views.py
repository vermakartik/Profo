from django.shortcuts import render, redirect
from Essentials.utils import userStatusDefined
from Student import forms

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user_status_value = userStatusDefined(request.user)
        if user_status_value == False:
            return redirect('user:user_status')
    return render(request, 'Essentials/home.html')

def user_status_define(request):
    if request.method == 'POST':
        return redirect('user:user_profile_form', user_status=request.POST['user_status'])
    elif request.method == "GET":
        return render(request, 'Essentials/user_status.html')


def user_profile_form(request, user_status):
    if user_status == 'student':
        return redirect('student:profile_form')