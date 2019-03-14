import logging

from werkzeug.exceptions import HTTPException as BaseHTTPException

from app.extensions.response_wrapper import wrap_response
from app import models as m

_logger = logging.getLogger(__name__)


class HTTPException(BaseHTTPException):
    def __init__(self, code=400, message=None, errors=None):
        super().__init__(description=message, response=None)
        self.code = code
        self.errors = errors


class BadRequestException(HTTPException):
    def __init__(self, message='Bad Request', errors=None):
        super().__init__(code=400, message=message, errors=errors)


class NotFoundException(HTTPException):
    def __init__(self, message='Resource Not Found', errors=None):
        super().__init__(code=404, message=message, errors=errors)


class UnAuthorizedException(HTTPException):
    def __init__(self, message='UnAuthorized', errors=None):
        super().__init__(code=401, message=message, errors=errors)


class ForbiddenException(HTTPException):
    def __init__(self, message='Permission Denied', errors=None):
        super().__init__(code=403, message=message, errors=errors)


def global_error_handler(e):
    # traceback.print_exc()
    m.db.session.rollback()
    _logger.error('rollback success')
    code = 500
    errors = None
    if isinstance(e, BaseHTTPException):
        code = e.code
    if isinstance(e, HTTPException):
        errors = e.errors
    res = wrap_response(None, str(e), code)
    if errors:
        res[0]['errors'] = errors
    return res
