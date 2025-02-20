from django.urls import path
from .views import get_all_teachers, teacher_details, add_teacher, update_teacher, delete_teacher

urlpatterns=[
    path('add-teacher/',add_teacher,name='add_teacher'),
    path('',get_all_teachers,name='teachers'),
    # path('teachers-details/',teacher_details,name="details"),
    path('teacher/<int:teacher_id>/', teacher_details, name="teacher_detail"),
    path('teacher/<int:teacher_id>/update/', update_teacher, name='update_teacher'),
    path('teachers/<int:teacher_id>/delete/',delete_teacher,name='delete_teacher')
]