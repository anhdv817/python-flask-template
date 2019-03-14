# coding=utf-8
import logging

from app.tests.api import APITestCase
from app import models as m

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


class UserApiTestCase(APITestCase):
    def url(self):
        return '/api/users/'

    def method(self):
        return 'POST'

    def test_success(self):
        uid = 1
        valid_data = {
            'id': uid,
            'username': 'admin',
            'email': 'admin@example.com',
            'password': 'secret',
            'role': 'admin'
        }
        rv = self.send_request(data=valid_data)
        saved_user = m.User.query.get(uid)  # type: m.User

        self.assertEqual(200, rv.status_code)
        assert saved_user
        self.assertEqual(saved_user.id, uid)
        self.assertEqual(saved_user.username, valid_data['username'])
        self.assertEqual(saved_user.email, valid_data['email'])
        self.assertEqual(saved_user.role, valid_data['role'])

    def test_invalid_data(self):
        invalid_data = {
            'id': 69,
            'username': 'moderator',
            'email': 'moderator',
            'password': 'terces',
            'role': 'moderator'
        }

        rv = self.send_request(data=invalid_data)
        self.assertEqual(400, rv.status_code)
