from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name="accounts"
urlpatterns = [
    path('register/', views.register, name="register"),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url('^',include('django.contrib.auth.urls')),
    path('verify_account/', views.verfiy_account, name="verify_account"),
    path('resend_verification_email/', views.resend_email, name='resend_email'),
]