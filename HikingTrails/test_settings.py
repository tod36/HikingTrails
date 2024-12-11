import os
from unittest import TestCase
from unittest.mock import patch


class TestGetEnv(TestCase):

    @patch.dict(os.environ,
                {'DJANGO_SETTINGS_MODULE': 'HikingTrails.settings', 'SECRET_KEY': 'test_secret_key', 'DEBUG': 'True',
                 'ALLOWED_HOSTS': 'localhost,127.0.0.1'})
    def test_environment_variables(self):
        from django.conf import settings

        self.assertEqual(settings.SECRET_KEY, 'test_secret_key')
        self.assertTrue(settings.DEBUG)
        self.assertEqual(settings.ALLOWED_HOSTS, ['localhost', '127.0.0.1'])
