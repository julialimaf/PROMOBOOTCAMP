

from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_email(subjects, from_email, to_email, template, context):
    message = render_to_string(template, context)

    email = EmailMessage(
       subjects,
        message,
        from_email,
        to_email,
    )
    email.content_subtype = 'html'
    email.send(fail_silently=False)