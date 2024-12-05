from django.test import TestCase
from .models import Trails
from HikingTrails.Hikers.models import Hiker
from django.contrib.auth.models import User

class TrailModelTest(TestCase):
    def setUp(self):
        user = Hiker.objects.create_user(username='testuser', password='12345')
        hiker = Hiker.objects.create(age=25, phone='123456789', address='Test Address')
        self.trail = Trails.objects.create(
            name='Test Trail',
            elevation_gain=57,
            length=10.5,
            difficulty='Moderate',
            hiker=hiker
        )

    def test_trail_creation(self):
        self.assertEqual(self.trail.name, 'Test Trail')
        self.assertEqual(self.trail.elevation_gain, 57)
        self.assertEqual(self.trail.length, 10.5)
        self.assertEqual(self.trail.difficulty, 'Moderate')

    def test_trail_string_representation(self):
        self.assertEqual(str(self.trail), 'Test Trail')