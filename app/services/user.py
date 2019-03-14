# coding=utf-8
import logging
import re

from app import models as m
from app import repositories
from app.extensions.exceptions import BadRequestException

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


def create_user(username, email, password, fullname="", role="", **kwargs):
    """
    Validate post data and create a new user
    :param str username:
    :param str email:
    :param str password:
    :param str fullname:
    :param str role:
    :param kwargs:
    :return: a new user
    :rtype: m.User
    """
    if (
        username and len(username) < 50 and
        email and re.match(r"[^@]+@[^\.]+\..+", email) and
        password and re.match(r"^[A-Za-z0-9]{6,}$", password)
    ):
        existed_user = repositories.user.find_one_by_email_or_username_ignore_case(email, username)
        if existed_user:
            raise BadRequestException(
                "User with username {username} "
                "or email {email} already existed!".format(
                    username=username,
                    email=email
                )
            )

        user = repositories.user.save_user_to_database(
            username=username,
            email=email,
            fullname=fullname,
            role=role,
            **kwargs
        )
        return user
    else:
        raise BadRequestException("Invalid user data specified!")

