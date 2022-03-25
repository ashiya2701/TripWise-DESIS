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

class Group(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        name=db.Column(db.String(150))
        description=db.Column(db.String(300))

class UserGroups(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        group=db.Column(db.Integer, ForeignKey(Group.id))
        user=db.Column(db.Integer, ForeignKey(User.id))        

class City(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        name=db.Column(db.String(150))
        state=db.Column(db.String(150))
        country=db.Column(db.String(150)) 

class Flight(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        src=db.Column(db.Integer, ForeignKey(City.id))
        dest= db.Column(db.Integer, ForeignKey(City.id))
        dur= db.Column(db.Float) 
        price =db.Column(db.Integer)
        
class Bus(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        src=db.Column(db.Integer, ForeignKey(City.id))
        dest= db.Column(db.Integer, ForeignKey(City.id))
        dur= db.Column(db.Float) 
        price =db.Column(db.Integer) 

class Trains(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        src=db.Column(db.Integer, ForeignKey(City.id))
        dest= db.Column(db.Integer, ForeignKey(City.id))
        dur= db.Column(db.Float) 
        price =db.Column(db.Integer)
        
class Hotels(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        city=db.Column(db.Integer, ForeignKey(City.id))
        price =db.Column(db.Integer)
        distancefromairport =db.Column(db.Integer) 
        distancefromrailways =db.Column(db.Integer) 
        timefromairport =db.Column(db.Float) 
        timefromrailways =db.Column(db.Float)

class Token(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        User=db.Column(db.Integer, ForeignKey(User.username))
        token= db.Column(db.String(150))

class Place(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        city=db.Column(db.Integer, ForeignKey(City.id))
        name=db.Column(db.String(150))
        xcordinate= db.Column(db.Integer)
        ycordinate= db.Column(db.Integer)

class Expense(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(150))
        amount = db.Column(db.Integer)
        group = db.Column(db.Integer, ForeignKey(Group.id))
        paid_by = db.Column(db.Integer, ForeignKey(User.id))

class UserExpense(db.Model):
        id=db.Column(db.Integer, primary_key=True)
        expense=db.Column(db.Integer, ForeignKey(Expense.id))
        user=db.Column(db.Integer, ForeignKey(User.id))
