from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', "")
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        