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

def student_profile(request):
        user_obj = User.objects.get(username = request.user)
        student_obj = None
        context_object = {}
        try:
                student_obj = models.StudentSummaryModel.objects.get(student_user = user_obj)
                context_object['profile'] = student_obj
                # print("Got Count -> {!s}".format(student_obj.studenttestmodel_set.all().count()))
                if student_obj.studenttestmodel_set.all().count() > 0:
                        not_attempt_test_count = student_obj.studenttestmodel_set.all().exclude(attempt_status=models.INT_ATTEMPTED).count()
                        context_object['not_attempt_count'] = not_attempt_test_count
                else:
                        context_object['not_attempt_count'] = 0
        except:
                redirect('404_not_found')
        print(student_obj)
        # {'profile': student_obj, 'not_attempt_count': }
        return render(request, 'Student/profile.html', context_object)

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
        student_id = User.objects.get(username = request.user)
        print(student_id)
        student_user = models.StudentSummaryModel.objects.get(student_user = student_id)
        print(student_id)
        prev_test_list = models.StudentTestModel.objects.filter(student_id = student_user, attempt_status = models.INT_ATTEMPTED, test_id__is_published = False)
        test_list = Test.objects.all().exclude(id__in = prev_test_list)
        return render(request, 'Student/test_list.html', {'test_list': test_list})

def test_join(request):
        print("test Joining Called!")
        test_id = request.GET.get('test_id')
        test = Test.objects.get(id = test_id)
        student_obj = models.StudentSummaryModel.objects.get(student_user = User.objects.get(username = request.user))
        student_test = models.StudentTestModel(student_id = student_obj, test_id = test)
        try:
                student_test.save()
        except IntegrityError as err:
                pass
        return redirect('student:test_list')

def test_attempt(request, test_id):
        if request.method == "POST":        
                print('Got Test Submitted')
                print(request.POST)
                student_score_obj = ctest_utils.evaluate(request.POST, test_id)
                student_score = student_score_obj['correct']
                test_obj = Test.objects.get(id = test_id)
                student_user_id = User.objects.get(username = request.user)
                student_id = models.StudentSummaryModel.objects.get(student_user = student_user_id)
                student_test = models.StudentTestModel.objects.get(student_id = student_id, test_id = test_obj)
                setattr(student_test, 'student_score', student_score)
                setattr(student_test, 'attempt_status', models.INT_ATTEMPTED)
                student_test.save()
                return redirect('student:after_test', test_id = test_id)
        test = Test.objects.get(id = test_id)
        print(test)
        return render(request, 'Student/test_attempt.html', {'test': test})

def after_test(request, test_id):
        test_model = models.StudentTestModel.objects.all().filter(test_id__id = test_id).filter(student_id__student_user__username = request.user)[0]
        context_obj = {}
        context_obj['student_score'] = test_model.student_score
        total_count = test_model.test_id.question_set.all().count()
        context_obj['total_count'] = total_count
        return render(request, 'Student/thankaftertest.html', context_obj)

def pervious_test(request):
        context_obj = {}
        student_id = User.objects.get(username = request.user)
        print(student_id)
        student_user = models.StudentSummaryModel.objects.get(student_user = student_id)
        print(student_id)
        tests_list = models.StudentTestModel.objects.filter(student_id = student_user, attempt_status = models.INT_ATTEMPTED)
        print(tests_list)
        context_obj['test_list'] = tests_list
        return render(request, 'Student/prev_test_list.html', context_obj)

