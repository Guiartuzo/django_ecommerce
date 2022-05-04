from django.test import SimpleTestCase, TestCase
from perfil.forms import PerfilForm, UserForm
from datetime import datetime
from django.contrib.auth.models import User


class TestForms(TestCase):

    def test_perfilform_valid_data(self):
        form = UserForm(data={
            'first_name':'test-user',
            'last_name' : 'test-user-lastname',
            'username' : 'test-user-username',
            'password' : '123456',
            'password2' : '123456',
            'email' : 'test@email.com',
        })

        self.assertTrue(form.is_valid())

    def test_perfilfom_no_data(self):
        form = PerfilForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),11)
