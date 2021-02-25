from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Group, Lecturer, Student


@receiver(pre_save, sender=Student, dispatch_uid='capitalize_name_student')
def capitalize_name_student(sender, instance, **kwargs):
    instance.first_name = str(instance.first_name).capitalize()
    instance.last_name = str(instance.last_name).capitalize()


@receiver(pre_save, sender=Lecturer, dispatch_uid='capitalize_name_lecturer')
def capitalize_name_lecturer(sender, instance, **kwargs):
    instance.first_name = str(instance.first_name).capitalize()
    instance.last_name = str(instance.last_name).capitalize()


@receiver(pre_save, sender=Group, dispatch_uid='capitalize_name_group')
def capitalize_name_group(sender, instance, **kwargs):
    instance.course = str(instance.course).capitalize()
