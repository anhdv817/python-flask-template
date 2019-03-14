# coding=utf-8
import logging
import pytest

__author__ = 'Kien'
_logger = logging.getLogger(__name__)


@pytest.fixture
def app_class(request, app):
    if request.cls is not None:
        request.cls.app = app
