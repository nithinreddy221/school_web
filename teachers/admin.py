from django.contrib import admin
# <<<<<<< HEAD

# Register your models here.
# =======
from .models import Teacher, TeacherStudentAssignment



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'hire_date', 'salary')
    list_editable = ('salary',)  # Fields that can be edited directly in the list view
    search_fields = ('first_name', 'last_name', 'email')  # Add a search bar
    list_filter = ('hire_date', 'salary')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherStudentAssignment)
# >>>>>>> fc4f10679c8470a68eb3fc5671721584cf8a97bc
