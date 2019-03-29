from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from Student import forms
from Student import models
from CTest.models import Test
from django.contrib.auth.models import User
from accounts import models as accounts_models
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from CTest import utils as ctest_utils

student_model_fields = [
        'studentRollNumber', 
        'student_first_name',
        'student_last_name', 
        'student_dob', 
        'student_gender', 
        'student_caste', 
        'student_father_first_name', 
        'student_father_last_name',
        'student_mother_first_name', 
        'student_mother_last_name', 
        'student_mobile', 
        'student_emergency_contact',
]

exceptional_fields = ['student_emergency_contact']
nested_fields = ['student_caste']

# Create your views here.
def __check_n_fill__(fields, data, contextVar):
        fieldsNotFound = []
        for field in fields:
                if field in data:
                        setattr(contextVar,field, data.get(field, ''))
                else:
                        fieldsNotFound.append(field)
        return (contextVar, fieldsNotFound)

def student_profile_post(request):
        print('profile post called')
        print(request.user)
        user_obj = User.objects.get(username = request.user)
        print(user_obj)
        student_obj = None
        try:
                student_obj = models.StudentSummaryModel.objects.get(student_user = user_obj)
                print(student_obj)   
        except:
                print('object not found')
        print(student_obj)
        return render(request, 'Student/profile.html', {'profile': student_obj})

def student_profile_form(request):
        if request.method == 'POST':
                print(request.POST)
                user_obj = User.objects.get(username=request.user)
                student_obj = models.StudentSummaryModel(student_user = user_obj)
                student_obj, fnf = __check_n_fill__(student_model_fields, request.POST, student_obj)
                student_obj.save()
                user_status = accounts_models.UserStatus.objects.get(user = user_obj)
                setattr(user_status, 'user_status', accounts_models.INT_STUDENT)
                user_status.save()
                print(student_obj)
                return redirect('student:profile')
        else:
                form_set = []
                form_set.append(forms.StudentSummaryModelForm())
                form_set.append(forms.StudentGeneralProfileModelForm())
                form_set.append(forms.StudentFamilyDetailsModelForm())
                form_set.append(forms.StudentContactDetailsModelForm())
                return render(request, 'Student/user_profile_form.html', {'form_set': form_set})
        

def getTestList(request):
    test_list = Test.objects.all()
    return render(request, 'Student/test_list.html', {'test_list': test_list})

def test_join(request):
        print("test Joining Called!")
        test_id = request.GET.get('test_id')
        test = Test.objects.get(id = test_id)
        student = models.StudentSummaryModel.objects.get(student_user = User.objects.get(username = request.user))
        student_test = models.StudentTestModel(student_id = student, test_id = test)
        try:
                student_test.save()
        except IntegrityError as err:
                pass
        return redirect('student:test_list')

def test_attempt(request, test_id):
        if request.method == "POST":        
                print('Got Test Submitted')
                print(request.POST)
                student_score = ctest_utils.evaluate(request.POST)
                print('type of request.user Object is -> ')
                print(type(request.user))
                test_obj = Test.objects.get(id = test_id)
                student_id = models.StudentSummaryModel.objects.get(student_user = User.objects.get(username = request.user))
                student_test = models.StudentTestModel.objects.get(student_id = student_id, test_id = test_obj)
                setattr(student_test, 'student_score', student_score)
                setattr(student_test, 'attempt_status', models.INT_ATTEMPTED)
                student_test.save()
                return redirect('student:after_test', test_id = test_id)
        test = Test.objects.get(id = test_id)
        print(test)
        return render(request, 'Student/test_attempt.html', {'test': test})

def after_test(request, test_id):
        return render(request, 'Student/thankaftertest.html')

