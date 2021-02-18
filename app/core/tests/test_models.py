from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='nathon@gmail.com', password='password'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'nathon@gmail.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        email = 'nathon@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'password')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_is_valid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'nathon@gmail.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='BBQ'
        )

        self.assertEqual(str(tag), tag.name)
