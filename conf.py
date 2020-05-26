import os

from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.abspath('templates')

app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY']= 'FUCKYOUALLLLLLLLLLLLIFUCKUUUUUUUUUUULICEUMLLLLL'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
admin = Admin(app, template_mode='bootstrap3')
migrate = Migrate(app, db)
