# coding=utf-8
import logging
import enum
import datetime

from flask_restplus import fields
from app.models import db, bcrypt, TimestampMixin

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)


class User(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'users'

    def __init__(self, **kwargs):
        """
        Support direct initialization
        :param kwargs:
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    class Role(enum.Enum):
        """
        Role of a user in the system.
        """
        admin = 'admin'
        moderator = 'moderator'
        viewer = 'viewer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(191), nullable=False, unique=True)
    username = db.Column(db.String(191), nullable=False, unique=True)
    fullname = db.Column(db.String(191), nullable=False)
    status = db.Column(db.Integer, default=1)
    password_hash = db.Column(db.String(100))
    id_token = db.Column(db.String(512), nullable=True)
    image = db.Column(db.Text(), nullable=True)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.viewer)
    last_login = db.Column(db.TIMESTAMP, default=datetime.datetime.now)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self):
        return True

    def to_dict(self):
        """
        Transform user obj into dict
        :return:
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'fullname': self.fullname,
            'status': self.status
        }


class UserSchema:
    user = {
        'id': fields.Integer(required=True, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'role': fields.String(required=False,
                              description='user role (admin|moderator|viewer)')
    }

    user_create_req = user.copy()
    user_create_req.pop('id', None)
    user_create_req.update({
        'password': fields.String(required=True, description='user password'),
    })
