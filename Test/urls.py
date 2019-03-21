from django.urls import path
from . import views

app_name="test"
urlpatterns = [
    path('new_test/', views.new_test, name="new_test"),
]
    