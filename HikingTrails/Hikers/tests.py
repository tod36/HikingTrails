from HikingTrails.Hikers.forms import HikerRegForm
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from HikingTrails.Hikers.models import Hiker

class HikerModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='12345',
            age=25,
            phone='123456789',
            address='Test Address'
        )

    def test_hiker_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.age, 25)
        self.assertEqual(self.user.phone, '123456789')
        self.assertEqual(self.user.address, 'Test Address')
        self.assertFalse(self.user.is_approved)

    def test_hiker_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')


class HikerRegFormTest(TestCase):
    def test_hiker_reg_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        }
        form = HikerRegForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_hiker_reg_form_invalid_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'password1': 'strongpassword123',
            'password2': 'differentpassword'
        }
        form = HikerRegForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


class HikerDeleteViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='12345'
        )
        self.hiker = Hiker.objects.create(
            age=25,
            phone='123456789',
            address='Test Address'
        )

    def test_get_hiker_delete_view(self):
        response = self.client.get(reverse('hiker_delete', args=[self.hiker.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hikers/hiker_delete.html')
        self.assertContains(response, self.hiker.username)

    def test_post_hiker_delete_view(self):
        response = self.client.post(reverse('hiker_delete', args=[self.hiker.id]))
        self.assertEqual(response.status_code, 302)
