from django.forms import ModelForm
from .models import Test, Question, Answer
from django.contrib.admin.widgets import AdminTimeWidget

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(BaseForm, self).__init__(*args, **kwargs)

class TestForm(BaseForm):
    class Meta:
        model = Test
        fields = ['test_name', 'available_time']
        widgets = {
            'available_time': AdminTimeWidget(attrs={'type': 'time', 'step': 60})
        }

class QuestionForm(BaseForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(BaseForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_answer_correct']