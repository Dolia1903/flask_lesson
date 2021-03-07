from django import forms

from .models import ContactAdmin, Group, Lecturer, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('course', 'student', 'teacher')


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactAdmin
        fields = ('first_name', 'last_name', 'email', 'message')
