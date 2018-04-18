from datetime import datetime

from app.db import db


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=True)
    user = db.Column(db.String(45), nullable=True)
    message = db.Column(db.String(2048), nullable=True)
    create_time = db.Column(db.DATETIME, nullable=True)

    def __init__(self, product_id, user, message):
        self.product_id = product_id
        self.user = user
        self.message = message
        self.create_time = datetime.now()
