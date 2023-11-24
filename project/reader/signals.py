from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from project import settings
from reader.models import Reader
from reader.tasks import greet


@receiver(post_save, sender=Reader)
def mail_sender(sender, instance, created, **kwargs):
    if created:
        greet(instance.name, instance.email)
