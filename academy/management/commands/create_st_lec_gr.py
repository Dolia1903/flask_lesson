import random

from academy.models import Group, Lecturer, Student

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create x new groups, y new students, z new lecturers'
    # Моя программа, в теории, должна уметь создавать произвольное кол-во
    # студентов, групп и лекторов
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
        new_students_ids_list = []   # Для привязки студентов к группе
        new_lecturers_ids_list = []  # Для привязки преподавателя к группе
        fake = Faker()

        for student in range(total_students):
            Faker.seed(student)
            Student.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   email=fake.email())
            Faker.seed(student)
            # Чтобы получить то же значение first_name=fake.first_name()
            new_student = Student.objects.get(first_name=fake.first_name())
            new_students_ids_list.append(new_student.student_id)

        for lecturer in range(total_lecturers):
            Faker.seed(lecturer + 100)
            # Чтобы не создавало такого же препода, как студента для 1 и тд
            Lecturer.objects.create(first_name=fake.first_name(),
                                    last_name=fake.last_name(),
                                    email=fake.email())
            Faker.seed(lecturer + 100)
            new_lecturer = Lecturer.objects.get(first_name=fake.first_name())
            new_lecturers_ids_list.append(new_lecturer.lecturer_id)

        for group in range(total_groups):
            # Faker.seed(group)
            # Строки 53, 64, 65, почему-то у меня не получается
            # использовать другой параметр course=fake.job(), который для
            # Faker.seed(group) был бы уникальным, выдает
            # academy.models.DoesNotExist: Group matching query does not exist.
            teacher = random.choice(new_lecturers_ids_list)
            Group.objects.create(course=fake.job(), teacher_id=teacher)
            counter = 0
            if len(new_students_ids_list) > 0:
                while total_students / total_groups > counter:
                    student = random.choice(new_students_ids_list)
                    # Faker.seed(group)
                    # group = Group.objects.get(course=fake.job())
                    group = Group.objects.get(teacher_id=teacher)
                    group.student.add(Student.objects.get(student_id=student))
                    new_students_ids_list.remove(student)
                    counter += 1
