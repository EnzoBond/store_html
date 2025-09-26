from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mercado.db"
app.config['SECRET_KEY'] = '9088350021a4583bd2ab9f4d'
db.init_app(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)


from app import routes