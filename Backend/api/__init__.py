from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from config import Config
from flask_cors import CORS, cross_origin


db = SQLAlchemy()
DB_NAME = "database.db"
BASE_DIR= os.path.dirname(os.path.abspath(__name__))

def create_app():
    print('h0')
    app = Flask(__name__)
    CORS(app)
    print('h1')
    cors = CORS(app, resource={
        r"/*":{
            "origins":"*"
        }
    })
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config.from_object(Config)
    
    db.init_app(app)
    print('h2')

    from models import User

    from auth import auth
    from cities import cities
    from populatePlaces import populatePlaces
    from itinerary import itinerary
    from group import group
    from expense_logs import expense_logs
    from hotel import hotel
    from sample import sample
    from populateHotels import populateHotels

    from planner import planner
    app.register_blueprint(planner,url_prefix='/')
    app.register_blueprint(cities, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(populatePlaces, url_prefix='/')
    app.register_blueprint(itinerary, url_prefix='/')
    app.register_blueprint(group, url_prefix='/')
    app.register_blueprint(hotel, url_prefix='/')    
    app.register_blueprint(sample, url_prefix='/')
    app.register_blueprint(expense_logs, url_prefix='/')
    app.register_blueprint(populateHotels, url_prefix='/')


    # print('h3')
    create_database(app)
    # print('h4')

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
