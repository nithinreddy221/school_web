from django.contrib import admin
# <<<<<<< HEAD

# Register your models here.
# =======
from .models import Student, Subject, Marks, Attendance


admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Marks)
admin.site.register(Attendance)
# >>>>>>> fc4f10679c8470a68eb3fc5671721584cf8a97bc
