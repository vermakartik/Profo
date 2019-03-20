from django.urls import path
from . import views

app_name="student"
urlpatterns = [
    path('profile_form/', views.student_profile_form, name="profile_form"),
    path('profile/', views.student_profile_post, name="profile"),
]
    