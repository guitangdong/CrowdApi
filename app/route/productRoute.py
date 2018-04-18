from app.auth.permissions import Permissions
from app.auth.roleLevel import RoleLevel
from app.db import *
from flask_restful import reqparse, Resource, fields, marshal_with
from . import api

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'describes': fields.String,
    'thumbnail': fields.String,
    'image': fields.String,
    'create_time': fields.DateTime(dt_format='iso8601'),
}

parser = reqparse.RequestParser(trim=True)
parser.add_argument('name', location=['json'], type=str)
parser.add_argument('describes', location=['json'], type=str)
parser.add_argument('thumbnail', location=['json'], type=str)
parser.add_argument('image', location=['json'], type=str)


class ProductsRoute(Resource):
    @marshal_with(product_fields)
    def get(self):
        return Product.query.order_by(Product.create_time.desc()).all()

    @Permissions(RoleLevel.admin)
    def post(self):
        args = parser.parse_args()
        db.session.add(Product(args.name, args.describes, args.thumbnail, args.image))
        db.session.commit()
        return None, 201


class ProductRoute(Resource):
    @marshal_with(product_fields)
    def get(self, product_id):
        return Product.query.filter_by(id=product_id).first_or_404()

    @Permissions(RoleLevel.admin)
    @marshal_with(product_fields)
    def put(self, product_id):
        args = parser.parse_args()
        Product.query.filter_by(id=product_id).update({'name': args.name, 'describes': args.describes,
                                                       'thumbnail': args.thumbnail, 'image': args.image})
        db.session.commit()
        return Product.query.filter_by(id=product_id).first_or_404()


api.add_resource(ProductsRoute, '/api/v1/products')
api.add_resource(ProductRoute, '/api/v1/products/<product_id>')
