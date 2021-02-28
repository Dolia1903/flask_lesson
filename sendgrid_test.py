SENDGRID_API_KEY='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'

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='azazeil@protonmail.com',
    to_emails='dolia1903@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
