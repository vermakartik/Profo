from django.urls import path
from . import views

app_name="user"
urlpatterns = [
    path('user_status/', views.user_status_define, name="user_status"),
    path('user_profile_form/<slug:user_status>', views.user_profile_form, name="user_profile_form"),
    path('home/', views.home, name='home'),
]
    