from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class PageTests(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'تماس با ما')

    def test_contact_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_post(self):
        response = self.client.post(reverse('contact'), {'name': 'علی', 'email': 'ali@example.com', 'message': 'سلام'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'پیام شما با موفقیت ثبت شد.')

    def test_contact_post_invalid(self):
        response = self.client.post(reverse('contact'), {'name': '', 'email': '', 'message': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_register_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_post(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'secret1234', 'password2': 'secret1234'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_password_mismatch(self):
        response = self.client.post(reverse('register'), {'username': 'u2', 'password1': 'aaa', 'password2': 'bbb'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='u2').exists())

    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        User.objects.create_user(username='m', password='pw123456')
        response = self.client.post(reverse('login'), {'username': 'm', 'password': 'pw123456'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

    def test_login_wrong_password(self):
        User.objects.create_user(username='m', password='pw123456')
        response = self.client.post(reverse('login'), {'username': 'm', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
