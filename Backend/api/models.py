from sqlalchemy import ForeignKey
from __init__ import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(10))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    
class City(db.Model):
       id=db.Column(db.Integer, primary_key=True)
       name=db.Column(db.String(150))
       state=db.Column(db.String(150))
       country=db.Column(db.String(150)) 

class Flight(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        To=db.Column(db.Integer, ForeignKey(City.id))
        dest= db.Column(db.Integer, ForeignKey(City.id))
        dur= db.Column(db.Float) 
        price =db.Column(db.Integer)
       