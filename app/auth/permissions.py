from functools import wraps

from flask import request
from jose import JWTError

from app.auth.crowdToken import decode
from app.auth.roleLevel import RoleLevel
from app.route import Result, app


@app.before_request
def before_request():
    print(request.headers)
#
#
# @app.after_request
# def after_request(response):
#     if response is not None:
#         response.headers['Access-Control-Allow-Origin'] = '*'
#         response.headers['Access-Control-Allow-Methods'] = 'POST'
#         response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return response


class Permissions:
    """
    :param role: RoleLevel
    """
    def __init__(self, role):
        self.role = role

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            result = Result()
            if token is None:
                if self.role != RoleLevel.guest:
                    result.error = "Not logged"
                    return result.__dict__, 401
            else:
                try:
                    payload = decode(token)
                except JWTError as e:
                    result.error = e.args[0]
                    return result.__dict__, 401
                if not RoleLevel.check(RoleLevel(payload.get("role")), self.role):
                    result.error = "No Permissions"
                    return result.__dict__, 403
            ret = fn(*args, **kwargs)
            return ret
        return wrapper

