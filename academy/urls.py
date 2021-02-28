from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_students),

    path('students', views.get_students, name='get_students'),
    path('students/<int:student_id>/', views.get_student, name='get_student'),
    path('students/<int:student_id>/edit/', views.edit_student,
         name='edit_student'),
    path('students/new', views.create_student, name='create_student'),
    path('students/<int:student_id>/delete/', views.delete_student,
         name='delete_student'),

    path('lecturers', views.get_lecturers, name='get_lecturers'),
    path('lecturers/<int:lecturer_id>/', views.get_lecturer,
         name='get_lecturer'),
    path('lecturers/<int:lecturer_id>/edit/', views.edit_lecturer,
         name='edit_lecturer'),
    path('lecturers/new', views.create_lecturer, name='create_lecturer'),
    path('lecturers/<int:lecturer_id>/delete/', views.delete_lecturer,
         name='delete_lecturer'),

    path('groups', views.get_groups, name='get_groups'),
    path('groups/<int:group_id>/', views.get_group, name='get_group'),
    path('groups/<int:group_id>/edit/', views.edit_group, name='edit_group'),
    path('groups/new', views.create_group, name='create_group'),
    path('groups/<int:group_id>/delete/', views.delete_group,
         name='delete_group'),

    path('students/contact_admin', views.contact_admin, name='contact_admin'),
    path('lecturers/contact_admin', views.contact_admin, name='contact_admin'),
    path('groups/contact_admin', views.contact_admin, name='contact_admin'),
]
