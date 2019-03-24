from django.urls import path
from . import views

app_name="ctest"
urlpatterns = [
    path('new_test/', views.new_test, name="new_test"),
    path('edit_test/<int:test_id>', views.edit_test, name = "edit_test"),
    path('view_test/<int:test_id>', views.view_test, name = "view_test"),
    path('<int:test_id>/new_question/', views.new_question, name="new_question"),
    # path('view_question/', views.view_question, name="new_question"),
]