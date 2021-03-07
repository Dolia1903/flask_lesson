# from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, \
    render

from .forms import ContactForm, GroupForm, LecturerForm, StudentForm
from .models import Group, Lecturer, Student


# def get_index(request):
#     return HttpResponse("Hello, World!")


def get_students(request):
    students = Student.objects.all().order_by('first_name')
    return render(request, 'academy/get_students.html', {'students': students})


def get_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'academy/get_student.html', {'student': student})


def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('get_student', student_id=student_id)

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_form.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student.delete()
    return redirect('get_students')


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('last_name')
    return render(request, 'academy/get_lecturers.html',
                  {'lecturers': lecturers})


def get_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    return render(request, 'academy/get_lecturer.html', {'lecturer': lecturer})


def edit_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.save()
            return redirect('get_lecturer', lecturer_id=lecturer_id)

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_form.html', {'form': form})


def delete_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    lecturer.delete()
    return redirect('get_lecturers')


def get_groups(request):
    groups = Group.objects.all().order_by('course')
    return render(request, 'academy/get_groups.html', {'groups': groups})


def get_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    teacher = get_object_or_404(Lecturer, lecturer_id=group.teacher_id)
    students = get_list_or_404(Student, group=group_id)

    context = {
        'group': group,
        'students': students,
        'teacher': teacher
    }

    return render(request, 'academy/get_group.html', context)


def edit_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=True)
            group.save()
            return redirect('get_group', group_id=group_id)

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_form.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    group.delete()
    return redirect('get_groups')


def create_student(request):
    students = Student.objects.all().order_by('first_name')
    new_student = None

    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=True)

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

    if request.method == 'GET':
        group_form = GroupForm()

    context = {
        'groups': groups,
        'new_group': new_group,
        'group_form': group_form,
    }

    return render(request, 'academy/new_group.html', context)


def contact_admin(request):
    new_message = None

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_message = contact_form.save(commit=True)

    if request.method == 'GET':
        contact_form = ContactForm()

    context = {
        'new_message': new_message,
        'contact_form': contact_form,
    }

    return render(request, 'academy/added_message.html', context)
