# Created by thanhpd on 3/13/2019
import logging
import unittest

import pytest

from app import models as m, repositories

_logger = logging.getLogger(__name__)

user_id = 1
username = 'admin'

db_user_data = {
    'id': user_id,
    'username': username,
    'fullname': 'Phan Thanh',
    'email': 'admin@example.com',
    'password': 'secret',
    'role': username
}


class UserRepositoryTestCase(unittest.TestCase):
    @pytest.fixture
    def setup(self, mocker):
        mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)

    def test_find_one_by_email_or_username_ignore_case_when_username_found_then_return_user(self):
        repositories.user.save_user_to_database(**db_user_data)
        m.User.query.get(user_id)  # type: m.User
        user = repositories.user.find_one_by_email_or_username_ignore_case('test@gmail.com', username)
        self.assertIsNotNone(user)
        self.assertEqual(user.id, user_id)

    def test_find_one_by_email_or_username_ignore_case_when_email_found_then_return_user(self):
        repositories.user.save_user_to_database(**db_user_data)
        m.User.query.get(user_id)  # type: m.User
        user = repositories.user.find_one_by_email_or_username_ignore_case('admin@example.com', 'thanh')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)

    def test_find_one_by_email_or_username_ignore_case_when_not_found_then_return_none(self):
        repositories.user.save_user_to_database(**db_user_data)
        m.User.query.get(user_id)  # type: m.User
        user = repositories.user.find_one_by_email_or_username_ignore_case('a@example.com', 'thanh')
        self.assertIsNone(user)
