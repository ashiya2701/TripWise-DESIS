from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "database.db"
BASE_DIR= os.path.dirname(os.path.abspath(__name__))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)

    from models import User

    from auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from sample import sample
    app.register_blueprint(sample, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists(os.path.join(BASE_DIR, 'database.db')):
        db.create_all(app=app)
        print('Created Database!')
