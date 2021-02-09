# from django.conf import settings
from django.db import models
# from django.utils import timezone


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE,
                                related_name='teacher_academy_set')
