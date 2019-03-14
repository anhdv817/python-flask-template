# Created by thanhpd on 3/11/2019
import logging
import unittest
from unittest.mock import patch

import pytest

from app.extensions.exceptions import BadRequestException
from app.services import user

_logger = logging.getLogger(__name__)


class UserServiceTest(unittest.TestCase):
    @pytest.fixture
    def setup(self, mocker):
        mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)

    def test_create_user_when_email_is_invalid_then_raise_bad_request_exception(self):
        with pytest.raises(BadRequestException) as excinfo:
            user.create_user('thanh', 'thanh', '123456', 'Phan Thanh', 'admin')
        self.assertEqual(excinfo.value.description, 'Invalid user data specified!')

    @patch('app.repositories.user.find_one_by_email_or_username_ignore_case')
    def test_create_user_when_user_existed_then_raise_bad_request_exception(self, fake_find_user):
        fake_find_user.return_value = 'Not null value'
        with pytest.raises(BadRequestException) as excinfo:
            user.create_user('thanh', 'thanh@teko.vn', '123456', 'Phan Thanh', 'admin')
        self.assertEqual(excinfo.value.description, 'User with username thanh or email thanh@teko.vn already existed!')
