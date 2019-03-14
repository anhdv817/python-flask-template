# coding=utf-8
import logging
from flask_restplus import Api
from flask import Blueprint

from app.extensions.exceptions import global_error_handler
from .user import ns as user_ns

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_bp,
    version='1.0',
    title='Boilerplate API',
    validate=False,
    # doc='' # disable Swagger UI
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    api.add_namespace(user_ns)
    app.register_blueprint(api_bp)
    api.error_handlers[Exception] = global_error_handler
