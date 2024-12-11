from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase

from HikingTrails.Hikers.utils import send_welcome_email

UserModel = get_user_model()


class UtilsTests(TestCase):
    def test_send_welcome_email(self):
        user = UserModel.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')

        send_welcome_email(user)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome to HikingTrails!')
        self.assertEqual(mail.outbox[0].to, [user.email])
        self.assertIn('Thank you for signing up for HikingTrails!', mail.outbox[0].body)
