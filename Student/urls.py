from django.urls import path
from . import views

app_name="student"
urlpatterns = [
    path('test_attempt/<int:test_id>', views.test_attempt, name ='test_attempt'),
    path('test_list/', views.getTestList, name="test_list"),
    path('test_join/', views.test_join, name='test_join'),
    path('profile_form/', views.student_profile_form, name="profile_form"),
    path('profile/', views.student_profile, name="profile"),
    path('test_submitted/<int:test_id>', views.after_test, name="after_test"),
]
    