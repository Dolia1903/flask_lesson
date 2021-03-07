from LMS.settings import SENDGRID_API_KEY

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from sendgrid import Mail, SendGridAPIClient

from .models import ContactAdmin, Group, Lecturer, Student
from .tasks import send_email


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


@receiver(post_save, sender=ContactAdmin)
def send_notification(sender, instance, **kwargs):
    send_email.delay(instance.to_dict())
