from django.http import HttpResponse
from django.shortcuts import render

from students.models import Student


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

