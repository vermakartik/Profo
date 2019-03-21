from django.urls import path
from . import views

app_name="teachers"
urlpatterns = [
    path('profile_form/', views.profile_form, name="profile_form"),
    path('profile/', views.profile, name="profile"),
]
    