from datetime import datetime

from app.db import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    describes = db.Column(db.String(1024), nullable=True)
    thumbnail = db.Column(db.String(1024), nullable=True)
    image = db.Column(db.TEXT, nullable=True)
    create_time = db.Column(db.DATETIME, nullable=True)

    def __init__(self, name, describes, thumbnail, image):
        self.name = name
        self.describes = describes
        self.thumbnail = thumbnail
        self.image = image
        self.create_time = datetime.now()



