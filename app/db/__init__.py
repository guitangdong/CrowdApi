from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .product import *
from .message import *
from .user import *
