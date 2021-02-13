from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import render

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
