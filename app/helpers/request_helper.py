# coding=utf-8
import logging
from app.extensions import reqparse

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)


class RequestHelper:
    pagination_params = reqparse.RequestParser(bundle_errors=True)
    pagination_params.add_argument(
        'page',
        type=int,
        help='Page number, starting from 1',
        required=False,
        default=1,
        location='args'
    )

    pagination_params.add_argument(
        'pageSize',
        type=int,
        help='Page size',
        required=False,
        default=10,
        location='args'
    )
