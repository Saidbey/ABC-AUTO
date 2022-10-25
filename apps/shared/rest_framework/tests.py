# Python
import os
import json
from unittest import TestCase

import pycodestyle
from PIL import Image
from django.urls import reverse
from rest_framework.test import APITestCase

from config import settings
from apps.shared.utils.check_files import get_files_for_checking

TEST_USER1 = 'test1@example.com'
TEST_USER2 = 'test2@example.com'
TEST_USER3 = 'test3@example.com'
TEST_USER4 = 'test4@example.com'
CURRENT_PASSWORD = 'current_password_123'
NEW_PASSWORD = 'new_password_123'
WRONG_PASSWORD = 'wrong_password_123'


def fake_image(size=(100, 100)):
    image = Image.new('RGB', size, 'white')
    image.save('media/tests.jpg')


class TestAuthMixin(object):
    auth_url = 'users:auth-login'

    def setUp(self):
        fake_image()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_token())

    def _authentication(self, username, password):
        assert self.auth_url, 'Define lazy auth_url, it will be user as reverse(auth_url)'
        url = reverse(self.auth_url)
        data = {'username': username, 'password': password}
        return self.client.post(url, data, format='json')

    def get_token(self, username=TEST_USER1, password=CURRENT_PASSWORD):
        response = self._authentication(username, password)
        return response.data['token']

    def set_user(self, username=TEST_USER1, password=CURRENT_PASSWORD):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.get_token(username, password))

    def anonymous(self):
        self.client.credentials(HTTP_AUTHORIZATION='')

    def set_token(self, token: str):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)


class BaseTest(TestAuthMixin, APITestCase):
    fixtures = [
        # TODO: write fixtures here
        'user.yaml',
        'file.yaml',
    ]
