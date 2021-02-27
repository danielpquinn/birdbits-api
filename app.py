from flask import Flask
from flask import jsonify
from flask import request

from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

import lib.jwt

app = Flask(__name__)

api = Api(app)

lib.jwt.initialize(app)

# Set up the Flask-JWT-Extended extension
app.config.from_pyfile("config.cfg")

db = SQLAlchemy(app)

from resources.user_registration import UserRegistration
from resources.user_login import UserLogin
from resources.transaction import Transaction

api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")
api.add_resource(Transaction, "/transaction")
