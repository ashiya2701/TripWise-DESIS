from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import Flight
from models import User, City
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, login_required, logout_user, current_user
import json
from sqlalchemy import insert

sample = Blueprint('sample', __name__)

@sample.route('/sample_check_data', methods=['GET', 'POST'])
def sampleCheckData():

    result= City.query.order_by(City.id).all()
    print("result: ", result)
    result2=Flight.query.order_by(Flight.id).all()
    print("Flights: ",result2)

    data=[
        ['Delhi','UT', 'India'],
        ['Mumbai','Maharastra','India' ],
        ['Hyderabad', 'Telangana','India' ],
        ['Banglore','Karnataka', 'India' ],
        ['Kolkata', 'WB', 'India'],
        ['Chandigarh','UT','India'],
        ['Surat','Gujrat','India'],
        ['Ahemdabad','Gujrat','India'],
        ['Patna','Bihar','India'],
        ['Jaipur','Rajasthan','India'],
        ['Guwahati','Assam','India'],
        ['Panaji','Goa','India'],
        ['Ranchi','Jharkhand','India'],
        ['Indore','MP','India'],
        ['Pune','Maharastra','India'],
        ['Bhubaneshwar','Odisha','Inida'],
        ['Ludhiana','Punjab','India'],
        ['Ajmer','Rajasthan','India'],
        ['Tiruchirapalli','Tamil Nadu','India'],
        ['Chennai','Tamil Nadu', 'India'],
        ['Shimla','HP','India'],
        ['Ooty','Tanmil Nadu','India'],
        ['Manali','HP','India'],
        ['Rishikesh','Uttrakhand','India']
        
     ]
    data2=[
        ['Delhi','Chandigarh',0.35,2999],
        ['Delhi','Mumbai',1.00,3999],
        ['Delhi','Hyderbad',1.25,3599],
        ['Delhi','Banglore',1.05,3599],
        ['Delhi','Kolkata',0.40,2599],
        ['Delhi','Guwahati',0.40,2599],
        ['Delhi','Surat',0.55,3599],
        ['Delhi','Ahmedabad',0.55,4599],
        ['Delhi','Patna',0.35,3599],
        ['Delhi','Jaipur',1.05,3599],
        ['Delhi','Ranchi',0.55,2599],
        ['Delhi','Indore',1.00,2999],
        ['Delhi','Pune',0.55,4999],
        ['Delhi','Panaji',0.55,5999],
        ['Delhi','Bhubaneshwar',0.45,2999],
        ['Delhi','Tiruchirapalli',1.00,3549],
        ['Delhi','Chennai',1.00,2999],
        ['Mumbai','Kolkata',1.00,4999],
        ['Mumbai','Hyderabad',0.35,2999],
        ['Mumbai','Banglore',0.35,3299],
        ['Mumbai','Chandigarh',1.00,3999],
        ['Mumbai','Chennai',0.45,2999],
        ['Mumbai','Surat',1.25,3999],
        ['Mumbai','Patna',1.00,2999],
        ['Mumbai','Ahemdabad',1.00,4999],
        ['Mumbai','Jaipur',2.00,6999],
        ['Mumbai','Pune',0.25,1999],
        ['Mumbai','Ranchi',1.00,4999],
        ['Mumbai','Panaji',0.25,5999],
        ['Mumbai','Guwahati',1.00,3999],
        ['Mumbai','Indore',0.55,3005],
        ['Mumbai','Delhi',1.00,3999],
        ['Hyderabad','Delhi',1.00,3999],
        ['Hyderabad','Kolkata',1.00,4999],
        ['Hyderabad','Mumbai',0.35,2999],
        ['Hyderabad','Banglore',0.25,2299],
        ['Hyderabad','Chennai',0.25,2999],
        ['Hyderabad','Surat',1.25,3999],
        ['Hyderabad','Pune',0.25,1999],
        ['Hyderabad','Tiruchirapalli',0.40,2549],
        ['Banglore','Delhi',1.00,3999],
        ['Banglore','Kolkata',1.00,4999],
        ['Banglore','Mumbai',0.35,2999],
        ['Banglore','Hyderabad',0.25,2299],
        ['Banglore','Chennai',0.25,2999],
        ['Banglore','Surat',1.25,3999],
        ['Banglore','Pune',0.25,1999],
        ['Banglore','Tiruchirapalli',0.40,2549],
        ['Chennai','Delhi',1.00,3999],
        ['Chennai','Kolkata',1.00,4999],
        ['Chennai','Mumbai',0.35,2999],
        ['Chennai','Hyderabad',0.25,2299],
        ['Chennai','Banglore',0.25,2999],
        ['Chennai','Surat',1.25,3999],
        ['Chennai','Pune',0.25,1999],
        ['Chennai','Tiruchirapalli',0.20,2049],
        ['Chandigarh','Delhi',0.30,2456],
        ['Chandigarh','Mumbai',0.55,2367],
        ['Chandigarh','Kolkata',1.20,2345],
        ['Chandigarh','Hyderabad',2,20,7821],
        ['Chandigarh','Surat',0.25,2345],
        ['Chandigarh','Pune',1.25,6345],
        ['Chandigarh','Chennai',2.25,7345],
        ['Chandigarh','Panaji',3.25,8345],
        ['Surat','Delhi',0.30,2456],
        ['Surat','Mumbai',0.55,2367],
        ['Surat','Kolkata',1.20,2345],
        ['Surat','Hyderabad',2.20,7821],
        ['Surat','Chandigarh',0.25,2345],
        ['Surat','Pune',1.25,6345],
        ['Surat','Ahemdabad',0.25,2345],
        ['Surat','Panaji',3.25,8345],
        ['Ahemdabad','Delhi',0.30,2456],
        ['Ahemdabad','Mumbai',0.55,2367],
        ['Ahemdabad','Surat',0.35,2367],
        ['Kolkata','Delhi',1.00,3999],
        ['Kolkata','Hyderabad',1.00,4999],
        ['Kolkata','Mumbai',0.35,2999],
        ['Kolkata','Guwahati',0.25,2299],
        ['Kolkata','Chennai',0.25,2999],
        ['Kolkata','Surat',1.25,3999],
        ['Kolkata','Patna',0.45,3999],
        ['Kolkata','Ranchi',0.35,2999],
        ['Kolkata','Bhubaneshwar',0.35,2999],
        ['Bhubaneshwar','Delhi',1.00,3999],
        ['Bhubaneshwar','Hyderabad',1.00,4999],
        ['Bhubaneshwar','Mumbai',0.35,2999],
        ['Bhubaneshwar','Guwahati',0.25,2299],
        ['Bhubaneshwar','Chennai',0.25,2999],
        ['Bhubaneshwar','Patna',0.45,3999],
        ['Bhubaneshwar','Ranchi',0.35,2999],
        ['Bhubaneshwar','Kolkata',0.35,2999], 
        ['Guwahati','Delhi',1.00,3999],
        ['Guwahati','Mumbai',0.35,2999],
        ['Guwahati','Bhubaneshwar',0.25,2299],
        ['Guwahati','Patna',0.45,3999],
        ['Guwahati','Kolkata',0.35,2999],
        ['Patna','Delhi',0.35,3999],
        ['Patna','Mumbai',0.55,2999],
        ['Patna','Bhubaneshwar',1.25,2299],
        ['Patna','Guwahati',0.45,3999],
        ['Patna','Kolkata',0.35,2999],
        ['Patna','Ranchi',0.25,2999],
        ['Ranchi','Delhi',0.35,3999],
        ['Ranchi','Mumbai',0.55,2999],
        ['Ranchi','Bhubaneshwar',1.25,2299],
        ['Ranchi','Guwahati',0.45,3999],
        ['Ranchi','Kolkata',0.35,2999],
        ['Ranchi','Patna',0.25,2999],
        ['Jaipur','Delhi',0.45,2899],
        ['Jaipur','Mumbai',1.00,4566],
        ['Jaipur','Chandigarh',0.40,2345],
        ['Jaipur','Indore',0.55,2456],
        ['Indore','Delhi',0.45,2899],
        ['Indore','Mumbai',1.00,4566],
        ['Indore','Chandigarh',0.40,2345],
        ['Indore','Jaipur',0.55,2456],
        ['Panaji','Mumbai',0.25,4567],
        ['Panaji','Delhi',1.25,8567],
        ['Panaji','Chennai',0.35,4567],
        ['Panaji','Banglore',0.35,5567],
        ['Tiruchirapalli','Hyderabad',0.25,4567],
        ['Tiruchirapalli','Banglore',1.25,2567],
        ['Tiruchirapalli','Chennai',0.35,2567],
        ['Pune','Delhi',1.30,3456],
        ['Pune','Mumbai',0.25,1367],
        ['Pune','Hyderabad',0.30,2821],
        ['Pune','Surat',1.25,6345],
        ['Pune','Panaji',1.25,4345],
        ['Pune','Hyderabad',0.25,4567],
        ['Pune','Banglore',1.25,2567],
        ['Pune','Chennai',0.35,2567]
    
        
        
     ]
        
        
        
    for entry in data:
        city=City.query.filter_by(name=entry[0]).first()
        
      #  print("line 28: ",city)
        if city:
            print("Exist")
            continue
        new_city= City(name=entry[0], state= entry[1], country=entry[2])
       # print(new_city)
        db.session.add(new_city)
    for record in data2:
        new_flight=Flight(src=record[0],dest=record[1],dur=record[2],price=record[3])
        db.session.add(new_flight)
            

    db.session.commit()

    result= City.query.order_by(City.id).all()
    result3=Flight.query.order_by(Flight.id).all()
    
    print("result: ", result)
    print("Flights: ",result3)
    response = Response(status=200)
    return response