from django.db import models
from students.models import Student, Subject

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    capable_subjects = models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TeacherStudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assigned_teachers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher} -> {self.student} ({self.subject})"
