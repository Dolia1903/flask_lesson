import random

from academy.models import Group, Lecturer, Student

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create x new groups, y new students, z new lecturers'

    # Моя программа умеет создавать:
    # 1) Произвольное кол-во студентов, лекторов и групп
    # (студенты распределяются равномерно по группам,
    # преподаватель для группые выбирается рандомный)
    # 2) Создавать только студентов
    # 3) Создавать только лекторов
    # 4) Создавать студентов и лекторов (без групп)
    # 5) Создавать лекторов и группы (без студентов)
    # 6) Если ввести только группы - выведет что без лектора нельзя

    # для теста - python manage.py create_st_lec_gr -ts 20 -tl 2 -tg 2

    def add_arguments(self, parser):
        parser.add_argument('-ts', type=int, help='Indicates the number of '
                                                  'students to be created')
        parser.add_argument('-tl', type=int, help='Indicates the number of '
                                                  'lecturer to be created')
        parser.add_argument('-tg', type=int, help='Indicates the number of '
                                                  'groups to be created')

    def handle(self, *args, **options):
        total_students = options['ts']
        total_lecturers = options['tl']
        total_groups = options['tg']
        new_students_ids_list = []  # Для привязки студентов к группе
        new_lecturers_ids_list = []  # Для привязки преподавателя к группе
        fake = Faker(use_weighting=False)
        # Чтобы снизить вероятность попадания тех же имен

        if total_students:  # Если указан хотя бы 1 студент -ts 1
            for student in range(total_students):
                Faker.seed(student)
                new_student = Student.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email()
                )
                new_students_ids_list.append(new_student.student_id)

        if total_lecturers:  # Если указан хотя бы 1 лектор -tl 1
            for lecturer in range(total_lecturers):
                Faker.seed(lecturer + 1000)
                # Чтобы не создавало такого же препода, как студента для 1 и тд
                new_lecturer = Lecturer.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email()
                )
                new_lecturers_ids_list.append(new_lecturer.lecturer_id)

        if total_groups:  # Если есть хотя бы 1 группа -tg 1 + указан лектор!
            for group in range(total_groups):
                if total_lecturers:
                    teacher = random.choice(new_lecturers_ids_list)
                    new_group = Group.objects.create(course=fake.job(),
                                                     teacher_id=teacher)
                else:
                    return "You can't create group without creating lecturer!"
                counter = 0  # Счетчик для равномерного распределения студентов
                if len(new_students_ids_list) > 0:
                    # Мы распределяем, пока не кончатся студенты
                    # + если они вообще были
                    while total_students / total_groups > counter:
                        student = random.choice(new_students_ids_list)
                        group = Group.objects.get(group_id=new_group.group_id)
                        group.student.add(Student.objects.get(
                            student_id=student)
                        )
                        new_students_ids_list.remove(student)
                        counter += 1
