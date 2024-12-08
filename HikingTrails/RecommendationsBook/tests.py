from django.contrib.auth.models import User
from django.test import TestCase

from HikingTrails.Hikers.models import Hiker
from .forms import BookRecommendationForm
from .models import BookRecommendation


class RecommendationsBookTest(TestCase):
    def setUp(self):
        user = Hiker.objects.create_user(username='testuser', password='12345')
        hiker = Hiker.objects.create(age=25, phone='123456789', address='Test Address')
        BookRecommendation.objects.create(hiker=hiker, title_message="Test Title", message="Test Message")

    def test_model_creation(self):
        recommendation = BookRecommendation.objects.get(title_message="Test Title")
        self.assertEqual(recommendation.message, "Test Message")


class BookRecommendationFormTest(TestCase):
    def setUp(self):
        user = Hiker.objects.create_user(username='testuser', password='12345')
        self.hiker = Hiker.objects.create(age=25, phone='123456789', address='Test Address')

    def test_book_recommendation_form_valid(self):
        form_data = {
            'hiker': self.hiker.id,
            'title_message': 'Test Title',
            'message': 'Test Message'
        }
        form = BookRecommendationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_book_recommendation_form_invalid(self):
        form_data = {
            'hiker': '',
            'title_message': '',
            'message': ''
        }
        form = BookRecommendationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('hiker', form.errors)
        self.assertIn('title_message', form.errors)
        self.assertIn('message', form.errors)
