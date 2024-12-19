import os
from unittest import TestCase
from unittest.mock import patch

import django
from django.core.mail import send_mail


class TestGetEnv(TestCase):

    @patch.dict(os.environ,
                {'DJANGO_SETTINGS_MODULE': 'HikingTrails.settings', 'SECRET_KEY': 'test_secret_key', 'DEBUG': 'True',
                 'ALLOWED_HOSTS': 'localhost,127.0.0.1'})
    def test_environment_variables(self):
        from django.conf import settings

        self.assertEqual(settings.SECRET_KEY, 'test_secret_key')
        self.assertTrue(settings.DEBUG)
        self.assertEqual(settings.ALLOWED_HOSTS, ['localhost', '127.0.0.1'])


# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HikingTrails.settings')
django.setup()


def test_send_mail():
    try:
        send_mail(
            subject="Test Email",
            message="This is a test email from HikingTrails.",
            from_email="todor36@gmail.com",
            recipient_list=["tod36@mail.bg"],
            fail_silently=False,
        )
        print("Test email sent successfully.")
    except Exception as e:
        print(f"Error sending test email: {e}")


if __name__ == "__main__":
    test_send_mail()
