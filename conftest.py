# coding=utf-8
import logging
import os

import pytest

import config

__author__ = 'Kien'
_logger = logging.getLogger(__name__)

TEST_DIR = os.path.join(config.ROOT_DIR, 'tests')


@pytest.fixture(autouse=True)
def app(request):
    from app import app
    from app.models import db

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # test db initializations go below here
    db.create_all()

    def teardown():
        db.session.remove()
        db.drop_all()
        ctx.pop()

    request.addfinalizer(teardown)
    return app
