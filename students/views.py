from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from students.models import Student
from students.forms import StudentForm


def sample(request):
    st = Student.objects.all()
    di = []
    for student in st:
        di.append([student.first_name, student.last_name, student.email, student.grade_level])

    return HttpResponse(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Students List</title>
</head>
<body>
<ul>
<li>{di[0][0]}</li>
<li>{di[0][1]}</li>
<li>{di[0][2]}</li>
<li>{di[0][3]}</li>
</ul>
<h1>{di[1]}</h1>
</body>
</html>""")



def get_all_students(request):
    print(request)
    stu = Student.objects.all()
    return render(request=request, template_name='all_students_list.html', context={'data':stu})


def get_singel_student(request, id):
    st = Student.objects.get(id=id)
    return render(request, 'student_data.html', {"st":st})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Adjust the redirect as needed
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

