from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from accounts.models import UserStatus
from accounts import models
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')   
            user = authenticate(username=username, password=raw_password)
            user_status = UserStatus(user=user, user_status=models.INT_NOT_DEFINED)
            user_status.save()
            print(user_status)
            login(request, user)
            return redirect('user:home')
    elif request.method == 'GET':
        form=CustomUserCreationForm()
    print(form)
    return render(request, 'accounts/register.html', {'form': form})