from django.urls import path

from students.views import sample

urlpatterns = [
    path('students/', sample, name="students")
]