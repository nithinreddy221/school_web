from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'grade_level', 'email']  # Customize fields to include
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
