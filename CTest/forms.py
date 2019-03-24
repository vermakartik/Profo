from django.forms import ModelForm
from .models import Test, Question, Answer

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['test_name']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_answer_correct']