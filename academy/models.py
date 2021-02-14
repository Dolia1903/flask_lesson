# from django.conf import settings
from django.db import models
# from django.utils import timezone


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=50)
    student = models.ManyToManyField(Student, blank=False)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE,
                                related_name='teacher_academy_set', blank=False)

    def __str__(self):
        return f'{self.course}'
