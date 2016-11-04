from flask import Flask
# from flask.ext.cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.basicauth import BasicAuth

app = Flask(__name__)
# CORS(app)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)

# basic_auth = BasicAuth(app)

# Imports views from __init__.py in respective packages
from oxnote import views
