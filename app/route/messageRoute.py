from flask import request

from app.db import *
from flask_restful import reqparse, Resource, fields, marshal_with
from . import api

message_fields = {
    'id': fields.Integer,
    'product_id': fields.Integer,
    'user': fields.String,
    'message': fields.String,
    'create_time': fields.DateTime(dt_format='iso8601'),
}

parser = reqparse.RequestParser(trim=True)
parser.add_argument('message', location=['json'], type=str)


class MessagesRoute(Resource):
    @marshal_with(message_fields)
    def get(self, product_id):
        return Message.query.filter_by(product_id=product_id).order_by(Message.create_time.desc()).all()

    def post(self, product_id):
        args = parser.parse_args()
        db.session.add(Message(product_id, request.remote_addr, args.message))
        db.session.commit()
        return None, 201


api.add_resource(MessagesRoute, '/api/v1/messages/<product_id>')
