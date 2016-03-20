from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.login as flask_login
app = Flask(__name__)

login_manager = flask_login.LoginManager()
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager.init_app(app)
app.secret_key = 'super secret string'
from app import views, models

