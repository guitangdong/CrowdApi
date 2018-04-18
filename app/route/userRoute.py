from sqlalchemy.exc import IntegrityError

from app.auth.permissions import Permissions
from app.auth.roleLevel import RoleLevel
from app.db import *
from flask_restful import reqparse, Resource, fields, marshal_with

from app.auth import crowdToken
from app.route.result import Result
from . import api

# user_fields = {
#     'id': fields.Integer,
#     'user_name': fields.String,
#     'password': fields.String,
#     'role': fields.String,
#     'create_time': fields.DateTime(dt_format='iso8601'),
# }

parser = reqparse.RequestParser(trim=True)
parser.add_argument('user_name', location=['json'], type=str)
parser.add_argument('password', location=['json'], type=str)


class LoginRoute(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        user = User.query.filter_by(user_name=args.user_name, password=args.password).first()
        if user is not None:
            result = Result()
            result.Authorization = crowdToken.encode(user.user_name, user.role)
            return result.__dict__, 200
        else:
            return None, 404


class RegisterRoute(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        try:
            db.session.add(User(args.user_name, args.password, RoleLevel.user.value))
            db.session.commit()
        except IntegrityError:
            return None, 409
        return None, 201


api.add_resource(LoginRoute, '/api/v1/login')
api.add_resource(RegisterRoute, '/api/v1/register')
