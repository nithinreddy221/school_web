from django.shortcuts import render, redirect, get_object_or_404

from teachers.forms import TeacherForm
from teachers.models import Teacher


# Create your views here.

def get_all_teachers(request):
    teachers=Teacher.objects.all()
    return render(request,'teachers.html', context={'data':teachers})


def add_teacher(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form=TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

def teacher_details(request,teacher_id):
    teacher=get_object_or_404(Teacher, id=teacher_id)
    return render(request,'teachers_details.html',{"teacher":teacher})
def update_teacher(request,teacher_id):
    teacher=get_object_or_404(Teacher,id=teacher_id)
    if request.method=="POST":
        form=TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', teacher_id=teacher.id)
    else:
        form=TeacherForm(instance=teacher)

    return render(request,"update_teacher.html",{'form':form, 'teacher':teacher})

def delete_teacher(request,teacher_id):
    teacher=get_object_or_404(Teacher,id=teacher_id)
    if request.method=="POST":
        teacher.delete()
        return redirect('teachers')
    return render(request,'update_teacher.html',{"teacher":teacher})