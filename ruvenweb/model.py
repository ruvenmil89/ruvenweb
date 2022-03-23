from ruvenweb import db
from flask_login import UserMixin
import sqlite3


class Feedback(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    email = db.Column(db.String(length=60), nullable=False, unique=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'




