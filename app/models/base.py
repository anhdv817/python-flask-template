# coding=utf-8
import logging
import datetime

import sqlalchemy as _sa
from sqlalchemy.ext.declarative import declared_attr

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


class TimestampMixin(object):
    """
    Adds `created_at` and `updated_at` common columns to a derived
    declarative model.
    """
    @declared_attr
    def created_at(self):
        return _sa.Column(_sa.TIMESTAMP,
                          default=datetime.datetime.now, nullable=False)

    @declared_attr
    def updated_at(self):
        return _sa.Column(_sa.TIMESTAMP, default=datetime.datetime.now)
