from flask import Flask
from flask_restful import Api

from app.db import db
from app.config.cfg import cfg
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = cfg.get('mysql.url')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, max_age=86400)

from .result import *
from .productRoute import *
from .messageRoute import *
from .userRoute import *

