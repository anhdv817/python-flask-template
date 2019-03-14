# coding=utf-8
import logging

from flask import request
import flask_restplus as _fr

from app import services, models
from app.extensions import Namespace

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)

ns = Namespace('users', description='User operations')

_user_res = ns.model('user_res', models.UserSchema.user)
_user_create_req = ns.model('user_create_req', models.UserSchema.user_create_req)


@ns.route('/', methods=['GET', 'POST'])
class Users(_fr.Resource):
    @ns.expect(_user_create_req, validate=True)
    @ns.marshal_with(_user_res)
    def post(self):
        """
        Create new user
        :return: list[User]
        """
        data = request.args or request.json
        user = services.user.create_user(**data)

        return user
