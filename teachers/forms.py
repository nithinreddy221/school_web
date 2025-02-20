from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields = ['first_name', 'last_name', 'email', 'salary', 'capable_subjects']
        widgets = {
            # 'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'capable_subjects': forms.CheckboxSelectMultiple(),
            # 'salary': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),  # Prevents negative numbers
        }

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary and salary < 0:
            raise forms.ValidationError("Salary must be a positive number.")
        return salary