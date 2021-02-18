from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import GroupForm, LecturerForm, StudentForm
from .models import Group, Lecturer, Student


def get_index(request):
    return HttpResponse("Hello, World!")


def get_students(request):
    students = Student.objects.all().order_by('first_name')
    return render(request, 'academy/get_students.html', {'students': students})


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('last_name')
    return render(request, 'academy/get_lecturers.html',
                  {'lecturers': lecturers})


def get_groups(request):
    groups = Group.objects.all().order_by('course')
    return render(request, 'academy/get_groups.html', {'groups': groups})


def create_student(request):
    students = Student.objects.all().order_by('first_name')
    new_student = None

    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=True)
            new_student.save()

    if request.method == 'GET':
        student_form = StudentForm()

    context = {
        'students': students,
        'new_student': new_student,
        'student_form': student_form,
    }

    return render(request, 'academy/new_student.html', context)


def create_lecturer(request):
    lecturers = Lecturer.objects.all().order_by('first_name')
    new_lecturer = None

    if request.method == 'POST':
        lecturer_form = LecturerForm(data=request.POST)
        if lecturer_form.is_valid():
            new_lecturer = lecturer_form.save(commit=True)
            lecturer_form.save()

    if request.method == 'GET':
        lecturer_form = LecturerForm()

    context = {
        'lecturers': lecturers,
        'new_lecturer': new_lecturer,
        'lecturer_form': lecturer_form,
    }

    return render(request, 'academy/new_lecturer.html', context)


def create_group(request):
    groups = Group.objects.all().order_by('course')
    new_group = None

    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=True)
            group_form.save()

    if request.method == 'GET':
        group_form = GroupForm()

    context = {
        'groups': groups,
        'new_group': new_group,
        'group_form': group_form,
    }

    return render(request, 'academy/new_group.html', context)
