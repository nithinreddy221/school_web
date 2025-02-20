from django.urls import path
from .views import student_list,student_create,student_delete,student_update,student_detail

urlpatterns = [
    # path('all/',student_list_create, name='student-list-create'),  # List & Create
    # path('students/<int:student_id>/',student_detail_update_delete, name='student-detail-update-delete'),  # Retrieve, Update, Delete
    # path('students-web/', student_list_view, name='student-web'),
    # path('web/', student_list_view, name='student-web'),
    path('list/', student_list, name='student-list'),  # GET all students
    path('create/', student_create, name='student-create'),  # POST new student
    path('update/<int:student_id>/', student_update, name='student-update'),  # PUT update student
    path('delete/<int:student_id>/', student_delete, name='student-delete'),
    path('details/<int:student_id>/', student_detail, name='student-detail'),

]