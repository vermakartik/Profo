from django.shortcuts import render, redirect
from .models import Test, Question, Answer
from django.http import JsonResponse
from .forms import TestForm, QuestionForm, AnswerForm
from Teachers import models as teacher_models
from django.contrib.auth.models import User
from django.forms import formset_factory
import datetime


# Create your views here.
def new_test(request):
    if request.method == "POST":
        user_obj = User.objects.get(username = request.user)
        print(request.POST)
        new_test = Test(test_name = request.POST.get('test_name', ""), available_time = datetime.datetime.strptime(request.POST.get('available_time'), '%H:%M').time())
        teacher_id = teacher_models.Teacher.objects.get(teacher_user = user_obj)
        setattr(new_test, 'teacher_id', teacher_id)
        new_test.save()
        return redirect('ctest:view_test', test_id=new_test.id)
    form = TestForm()
    print(form)
    return render(request, 'CTest/new_test.html', {'form': form})

def edit_test(request, test_id):
    if request.method == 'POST':
        test = Test.objects.get(id = test_id)
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save()
        else:
            test = Test.objects.get(id=test_id)
            form = TestForm(instance=test)
            print("\n\n----**---error Saving")
            return render(request, 'CTest/edit_test.html', {'test': test, 'form': form, 'error': "Error While Saving"})
        return redirect('ctest:view_test', test_id = test.id)
    test = Test.objects.get(id=test_id)
    form = TestForm(instance=test)
    return render(request, 'CTest/edit_test.html', {'test': test, 'form': form})

def view_test(request, test_id):
    test = Test.objects.get(id = test_id)
    return render(request, 'CTest/view_test.html', {'test': test})

def new_question(request, test_id):
    if request.method == 'POST':
        print(request.POST)
        test =  Test.objects.get(id = test_id)
        question = Question(test_id=test)
        setattr(question, 'question_text', request.POST.get('question_text', ""))
        question.save()
        is_answer_set_to_correct = False
        for index in range(4):
            answer = Answer(
                question_id = question,
                answer_text = request.POST.get('form-{!s}-answer_text'.format(index))
            )
            if 'form-{!s}-is_answer_correct'.format(index) in request.POST:
                if is_answer_set_to_correct == False:
                    setattr(answer, 'is_answer_correct', True)
                    is_answer_set_to_correct = True
                else:
                    setattr(answer, 'is_answer_correct', False)
            else:
                setattr(answer, 'is_answer_correct', False)
            answer.save()
        if is_answer_set_to_correct == False:
            return redirect("ctest:edit_question", test_id = test.id, question_id = question.id)
        return redirect('ctest:view_test', test_id = test.id)
    question_form = QuestionForm()
    answer_form_set = formset_factory(AnswerForm, extra=4)
    return render(request, 'CTest/new_question.html', {'question_form': question_form, 'answer_form_set': answer_form_set, "test_id": test_id})

def edit_question(request, test_id, question_id):
    if request.method == 'POST':
        print(request.POST)
        test =  Test.objects.get(id = test_id)
        question = Question.objects.get(id=question_id)
        setattr(question, 'question_text', request.POST.get('question_text', ""))
        question.save()
        answer_correct = False
        answer_set = question.answer_set.all()
        for ans in answer_set:
            ans.delete()
        for index in range(4):
            answer = Answer(
                question_id = question,
                answer_text = request.POST.get('form-{!s}-answer_text'.format(index))
            )
            if 'form-{!s}-is_answer_correct'.format(index) in request.POST:
                if answer_correct == False:
                    setattr(answer, 'is_answer_correct', True)
                    answer_correct = True
                else:
                    setattr(answer, 'is_answer_correct', False)
            else:
                setattr(answer, 'is_answer_correct', False)
            answer.save()
        if answer_correct == False:
            return redirect("ctest:edit_question", test_id = test.id, question_id = question.id)
        return redirect('ctest:view_test', test_id = test.id)
    test =  Test.objects.get(id = test_id)
    question = Question.objects.get(id=question_id)
    print(question)
    # print(answer_set)
    question_form = QuestionForm(initial = {'question_text': question.question_text}) 
    AnswerFormSet  = formset_factory(AnswerForm, extra = 0)
    answer_form_set = AnswerFormSet(initial = [
            {'answer_text': ans.answer_text, 'is_answer_correct' : ans.is_answer_correct} for ans in question.answer_set.all()
        ])
    return render(request, 'CTest/edit_question.html', {'question_form': question_form, 'answer_form_set': answer_form_set, "test_id": test_id, 'question_id': question.id})

def publish_test(request, test_id):
    test = Test.objects.get(id = test_id)
    setattr(test, 'is_published', True)
    test.save()
    return redirect('ctest:view_test', test_id = test_id)
