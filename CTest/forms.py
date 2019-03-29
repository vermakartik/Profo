from django.forms import ModelForm
from .models import Test, Question, Answer

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(BaseForm, self).__init__(*args, **kwargs)

class TestForm(BaseForm):
    class Meta:
        model = Test
        fields = ['test_name']

class QuestionForm(BaseForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(BaseForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_answer_correct']