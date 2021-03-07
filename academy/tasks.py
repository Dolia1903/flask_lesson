from datetime import date, timedelta
from time import sleep

from LMS.settings import SENDGRID_API_KEY

from celery import shared_task

from django.template.loader import render_to_string

from logger.models import Log

from sendgrid import Mail, SendGridAPIClient


@shared_task
def send_email(data):
    context = {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'message': data['message']
    }
    content = render_to_string('emails/added_message.html', context)
    message = Mail(
        from_email='azazeil@protonmail.com',
        to_emails='dolia1903@gmail.com',
        subject='New contact message',
        html_content=content
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)


@shared_task
def delete_yesterday_logs():
    yesterday_date = date.today() - timedelta(days=1)
    # yesterday_date = date.today()
    # это для тестов
    yesterday_logs = Log.objects.filter(
        created__day=yesterday_date.strftime('%d')
    )
    yesterday_logs.delete()
