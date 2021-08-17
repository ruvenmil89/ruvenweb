from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser
import os


SECRET_KEY = os.urandom(32)

config = configparser.ConfigParser()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ruvenweb.db'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)


from ruvenweb import routes


