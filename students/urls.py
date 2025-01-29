from django.urls import path

from students import views as st

urlpatterns = [
    path('st/', st.sample, name="st"),
    path('students/', st.get_all_students, name="students"),
    path('student/<int:id>/', st.get_singel_student, name="student"),
    path('add/', st.add_student, name='add_student')
]