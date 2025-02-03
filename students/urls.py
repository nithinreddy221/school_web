from django.urls import path

from students import views as st

urlpatterns = [
    path('st/', st.sample, name="st"),
    path('students/', st.get_all_students, name="students"),
    path('student/<int:id>/', st.get_singel_student, name="student"),
    path('add/', st.add_student, name='add_student'),
    path('update/<int:student_id>/', st.update_student, name='update_student'),
    path('patch/<int:student_id>/', st.patch_student, name='patch_student'),
    path('delete/<int:student_id>/', st.delete_student, name='delete_student'),
]