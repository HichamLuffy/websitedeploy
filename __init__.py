#!/usr/bin/python3
"""quiz app """


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

import sys

# Append the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


app = Flask(__name__)
app.config['SECRET_KEY'] = '5e930833f20b0d4a5fa7505d70f5aa80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/AQZ'
app.config['UPLOAD_FOLDER'] = 'static/images/quizzes'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login_page'

from websitedeploy import routes
