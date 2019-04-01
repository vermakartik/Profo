from django.shortcuts import render, redirect
from .forms import TeacherSummaryForm
from .models import Teacher
from django.contrib.auth.models import User
from accounts.models import UserStatus
from Student.models import StudentTestModel, StudentSummaryModel
from Student import models as student_models
from accounts import models as accounts_models
from CTest import models as ctest_models

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
    user_obj = User.objects.get(username = request.user)
    profile = Teacher.objects.get(teacher_user = user_obj)
    return render(request, 'Teachers/profile.html', {'profile': profile})

def check_permission_list(request):
    context_object = {}
    if 'permission_item' in request.GET and 'permission_status' in request.GET and 'student_id' in request.GET:
        get_test_id = request.GET.get('permission_item')
        get_student_roll_number = request.GET.get('student_id')
        get_perm_status = request.GET.get('permission_status')
        studenttest = StudentTestModel.objects.get(id = get_test_id)
        print(studenttest)
        
        if get_perm_status == 'GRANTED':
            setattr(studenttest, 'is_permitted', student_models.INT_PERMITTED)
        elif get_perm_status == 'REJECTED':
            setattr(studenttest, 'is_permitted', student_models.INT_NOT_PERMITTED)
        try:
            studenttest.save()
        except Exception as err:
            context_object['error'] = err
        return redirect('teachers:permission_list')

    user_obj = User.objects.get(username = request.user)
    teacher_id = Teacher.objects.get(teacher_user = user_obj)
    test_permission = StudentTestModel.objects.filter(test_id__teacher_id=teacher_id, is_permitted=student_models.INT_REQUESTED)
    context_object['permission_list'] = test_permission
    return render(request, 'Teachers/test_permission_list.html', context_object)