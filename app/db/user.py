from datetime import datetime

from app.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(36), unique=True, nullable=True)
    password = db.Column(db.String(36), nullable=True)
    role = db.Column(db.String(36), nullable=True)
    create_time = db.Column(db.DATETIME, nullable=True)

    def __init__(self, user_name, password, role):
        self.user_name = user_name
        self.password = password
        self.role = role
        self.create_time = datetime.now()
