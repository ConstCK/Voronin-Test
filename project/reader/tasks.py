from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from project import settings
from project.celery import app


@app.task
def greet(reader, email):
    html_content = render_to_string('greeting_mail.html', {
        'reader': reader,
    })

    msg = EmailMultiAlternatives(subject='Приветствие',
                                 body='',
                                 from_email=settings.DEFAULT_FROM_EMAIL,
                                 to=[email, ])

    msg.attach_alternative(html_content, 'text/html')

    msg.send()