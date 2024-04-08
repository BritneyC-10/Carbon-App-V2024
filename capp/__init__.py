from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)

# secret key
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

# database-configurations
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
application.config["SQLALCHEMY_BINDS"] = {"transport" : "sqlite:///transport.db"}
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # removes error-message
db = SQLAlchemy(application)

# encrypting passwords in database
bcrypt = Bcrypt(application)

# flask login-manager
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_calc.routes import carbon_calc
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_calc)
application.register_blueprint(users)
