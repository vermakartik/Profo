from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, SignUpForm, PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from accounts.models import UserStatus
from accounts import models
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')   
            user = authenticate(username=username, password=raw_password)
            user_status = UserStatus(user=user, user_status=models.INT_NOT_DEFINED)
            user_status.save()

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # messages
            current_site = get_current_site(request)
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
            })

            mail_subject = 'Activate your Profo portal account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            print(user_status)
            login(request, user)
            # return redirect('user:home')
            return HttpResponse('Thank you for your creating Profo Portal account. Verification Link has been send to your email account.')
    elif request.method == 'GET':
        form=SignUpForm()
    print(form)
    return render(request, 'accounts/register.html', {'form': form})

def activate(request, uid, token):
    try:
        # uid1 = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if  user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
        