# coding=utf-8
import logging
from sqlalchemy import or_

from app import models as m

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


def save_user_to_database(**kwargs):
    """
    Create new user record in database from validated data.
    :param kwargs:
    :return:
    """
    user = m.User(**kwargs)
    m.db.session.add(user)

    return user


def find_one_by_email_or_username_ignore_case(email, username):
    """
        Return a user instance if match, else None
        :param str email:
        :param str username:
        :return: a user instance
        :rtype: m.User
    """
    user = m.User.query.filter(
        or_(
            m.User.username == username,
            m.User.email == email
        )
    ).first()  # type: m.User

    return user or None

