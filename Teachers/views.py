from django.shortcuts import render, redirect
from .forms import TeacherSummaryForm
from .models import Teacher
from django.contrib.auth.models import User
from accounts.models import UserStatus
from accounts import models as accounts_models

# Create your views here.
def profile_form(request):
    if request.method == 'POST':
        user_obj = User.objects.get(username = request.user)
        teacher_obj = Teacher(teacher_user = user_obj)
        form = TeacherSummaryForm(request.POST, instance=teacher_obj)
        if form.is_valid():
            teacher_obj = form.save()
            print(teacher_obj)
            user_status = UserStatus.objects.get(user=user_obj)
            setattr(user_status, 'user_status', accounts_models.INT_TEACHER)
            user_status.save()
        else:
            print('error saving form')
            form = TeacherSummaryForm()
            return render(request, 'Teachers/profile_form.html', {'form': form, 'error': 'Error Saving Form!'})
        return redirect('teachers:profile')
    else:
        form = TeacherSummaryForm()
        return render(request, 'Teachers/profile_form.html', {'form': form})

def profile(request):
    user_obj = User(username = request.user)
    profile = Teacher(teacher_user = user_obj)
    return render(request, 'Teachers/profile.html', {'profile': profile})