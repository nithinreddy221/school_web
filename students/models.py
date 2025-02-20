from django.db import models
#
# <<<<<<< HEAD
# # Create your models here.
# =======
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    grade_level = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.IntegerField()
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} ({self.marks_obtained}/{self.max_marks})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status_choices = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused'),
    ]
    status = models.CharField(max_length=1, choices=status_choices)

    def __str__(self):
        return f"{self.student} - {self.date}: {self.get_status_display()}"
# >>>>>>> fc4f10679c8470a68eb3fc5671721584cf8a97bc
