from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', "")
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=256, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
