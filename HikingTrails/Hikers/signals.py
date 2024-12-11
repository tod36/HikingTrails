import logging

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()
logger = logging.getLogger(__name__)


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Welcome to HikingTrails!",
            message="Thank you for signing up for HikingTrails! We hope you enjoy our app!",
            from_email="todor36@gmail.com",
            recipient_list=[instance.email],
            fail_silently=False,
        )
