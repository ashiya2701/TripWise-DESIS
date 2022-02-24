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
    result3=Bus.query.order_by(Bus.id).all()
    print("Bus: ",result3)
    result4=Trains.query.order_by(Train.id).all()
    print("Train: ",result4)
    result5=Hotels.query.order_by(Hotel.id).all()
    print("Hotel: ",result5)
    

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
    data3 = [
        ['Delhi','Chandigarh',1.25,1988],
        ['Delhi','Mumbai',2.25,2999],
        ['Delhi','Hyderbad',2.5,4599],
        ['Delhi','Banglore',3.05,2499],
        ['Delhi','Kolkata',1.50,1999],
        ['Delhi','Guwahati',1.55,599],
        ['Delhi','Surat',2.00,1599],
        ['Delhi','Ahmedabad',1.55,2599],
        ['Delhi','Patna',1.25,1599],
        ['Delhi','Jaipur',2.25,1599],
        ['Delhi','Ranchi',1.55,599],
        ['Delhi','Indore',3.05,999],
        ['Delhi','Pune',2.55,2999],
        ['Delhi','Panaji',1.25,3999],
        ['Delhi','Bhubaneshwar',1.35,999],
        ['Delhi','Tiruchirapalli',2.45,1549],
        ['Delhi','Chennai',3.05,999],
        ['Mumbai','Kolkata',2.55,2999],
        ['Mumbai','Hyderabad',2.35,999],
        ['Mumbai','Banglore',1.55,1299],
        ['Mumbai','Chandigarh',2.45,1999],
        ['Mumbai','Chennai',2.00,999],
        ['Mumbai','Surat',2.35,1999],
        ['Mumbai','Patna',1.55,999],
        ['Mumbai','Ahemdabad',2.00,2999],
        ['Mumbai','Jaipur',4.00,4999],
        ['Mumbai','Pune',1.35,599],
        ['Mumbai','Ranchi',2.55,2999],
        ['Mumbai','Panaji',1.00,3999],
        ['Mumbai','Guwahati',2.25,1999],
        ['Mumbai','Indore',1.35,2005],
        ['Mumbai','Delhi',2.25,1999],
        ['Hyderabad','Delhi',2.35,1999],
        ['Hyderabad','Kolkata',3.05,2999],
        ['Hyderabad','Mumbai',1.55,999],
        ['Hyderabad','Banglore',2.00,299],
        ['Hyderabad','Chennai',1.55,999],
        ['Hyderabad','Surat',3.00,1999],
        ['Hyderabad','Pune',2.00,599],
        ['Hyderabad','Tiruchirapalli',1.25,1549],
        ['Banglore','Delhi',2.55,1999],
        ['Banglore','Kolkata',2.55,2999],
        ['Banglore','Mumbai',2.00,999],
        ['Banglore','Hyderabad',1.55,299],
        ['Banglore','Chennai',2.35,999],
        ['Banglore','Surat',3.00,1999],
        ['Banglore','Pune',2.05,599],
        ['Banglore','Tiruchirapalli',1.55,549],
        ['Chennai','Delhi',2.35,1999],
        ['Chennai','Kolkata',3.00,2999],
        ['Chennai','Mumbai',2.00,999],
        ['Chennai','Hyderabad',2.05,299],
        ['Chennai','Banglore',2.25,999],
        ['Chennai','Surat',3.05,1999],
        ['Chennai','Pune',2.55,799],
        ['Chennai','Tiruchirapalli',1.55,749],
        ['Chandigarh','Delhi',2.05,656],
        ['Chandigarh','Mumbai',2.55,867],
        ['Chandigarh','Kolkata',3.00,845],
        ['Chandigarh','Hyderabad',4.00,5821],
        ['Chandigarh','Surat',2.25,745],
        ['Chandigarh','Pune',3.05,4345],
        ['Chandigarh','Chennai',4.35,5345],
        ['Chandigarh','Panaji',5.05,6345],
        ['Surat','Delhi',1.55,756],
        ['Surat','Mumbai',3.05,867],
        ['Surat','Kolkata',3.45,645],
        ['Surat','Hyderabad',4.35,5821],
        ['Surat','Chandigarh',2.00,645],
        ['Surat','Pune',4.00,4345],
        ['Surat','Ahemdabad',2.55,745],
        ['Surat','Panaji',5.35,6345],
        ['Ahemdabad','Delhi',2.15,856],
        ['Ahemdabad','Mumbai',1.55,767],
        ['Ahemdabad','Surat',1.55,667],
        ['Kolkata','Delhi',3.25,1999],
        ['Kolkata','Hyderabad',3.55,2999],
        ['Kolkata','Mumbai',2.05,999],
        ['Kolkata','Guwahati',2.55,899],
        ['Kolkata','Chennai',3.25,999],
        ['Kolkata','Surat',3.25,1999],
        ['Kolkata','Patna',2.45,1999],
        ['Kolkata','Ranchi',2.05,999],
        ['Kolkata','Bhubaneshwar',2.35,999],
        ['Bhubaneshwar','Delhi',3.25,1999],
        ['Bhubaneshwar','Hyderabad',2.45,2999],
        ['Bhubaneshwar','Mumbai',1.55,999],
        ['Bhubaneshwar','Guwahati',2.05,899],
        ['Bhubaneshwar','Chennai',1.55,999],
        ['Bhubaneshwar','Patna',2.05,1999],
        ['Bhubaneshwar','Ranchi',2.15,999],
        ['Bhubaneshwar','Kolkata',1.55,999], 
        ['Guwahati','Delhi',2.45,1999],
        ['Guwahati','Mumbai',2.05,999],
        ['Guwahati','Bhubaneshwar',1.55,799],
        ['Guwahati','Patna',2.15,1999],
        ['Guwahati','Kolkata',2.05,999],
        ['Patna','Delhi',2.45,1999],
        ['Patna','Mumbai',2.55,999],
        ['Patna','Bhubaneshwar',3.05,799],
        ['Patna','Guwahati',2.25,1999],
        ['Patna','Kolkata',2.00,999],
        ['Patna','Ranchi',1.45,999],
        ['Ranchi','Delhi',1.55,1999],
        ['Ranchi','Mumbai',2.00,999],
        ['Ranchi','Bhubaneshwar',3.00,799],
        ['Ranchi','Guwahati',2.25,1999],
        ['Ranchi','Kolkata',1.45,999],
        ['Ranchi','Patna',2.00,999],
        ['Jaipur','Delhi',2.25,899],
        ['Jaipur','Mumbai',3.05,2566],
        ['Jaipur','Chandigarh',2.55,545],
        ['Jaipur','Indore',2.00,656],
        ['Indore','Delhi',2.35,899],
        ['Indore','Mumbai',3.00,2566],
        ['Indore','Chandigarh',1.45,745],
        ['Indore','Jaipur',3.00,856],
        ['Panaji','Mumbai',2.35,2567],
        ['Panaji','Delhi',2.25,6567],
        ['Panaji','Chennai',2.55,2567],
        ['Panaji','Banglore',1.45,3567],
        ['Tiruchirapalli','Hyderabad',2.05,2567],
        ['Tiruchirapalli','Banglore',3.00,867],
        ['Tiruchirapalli','Chennai',2.55,967],
        ['Pune','Delhi',3.45,1456],
        ['Pune','Mumbai',2.45,467],
        ['Pune','Hyderabad',1.45,821],
        ['Pune','Surat',3.35,4345],
        ['Pune','Panaji',3.45,2345],
        ['Pune','Hyderabad',2.35,2567],
        ['Pune','Banglore',3.25,767],
        ['Pune','Chennai',2.05,867]
    ]
        
    data4 = [
        ['Delhi','Chandigarh',1.25,1999],
        ['Delhi','Mumbai',2.25,2999],
        ['Delhi','Hyderbad',2.50,2599],
        ['Delhi','Banglore',3.30,2599],
        ['Delhi','Kolkata',2.05,1599],
        ['Delhi','Guwahati',1.55,1599],
        ['Delhi','Surat',2.05,2599],
        ['Delhi','Ahmedabad',1.35,3599],
        ['Delhi','Patna',2.25,2599],
        ['Delhi','Jaipur',3.05,2599],
        ['Delhi','Ranchi',2.00,1599],
        ['Delhi','Indore',2.25,1999],
        ['Delhi','Pune',1.35,3999],
        ['Delhi','Panaji',1.45,4999],
        ['Delhi','Bhubaneshwar',2.05,1999],
        ['Delhi','Tiruchirapalli',2.25,2549],
        ['Delhi','Chennai',3.25,1999],
        ['Mumbai','Kolkata',2.25,3999],
        ['Mumbai','Hyderabad',2.55,1999],
        ['Mumbai','Banglore',3.05,2299],
        ['Mumbai','Chandigarh',2.35,2999],
        ['Mumbai','Chennai',2.35,1999],
        ['Mumbai','Surat',3.05,2999],
        ['Mumbai','Patna',2.35,1999],
        ['Mumbai','Ahemdabad',2.00,3999],
        ['Mumbai','Jaipur',3.00,5999],
        ['Mumbai','Pune',1.25,999],
        ['Mumbai','Ranchi',2.00,3999],
        ['Mumbai','Panaji',1.25,4999],
        ['Mumbai','Guwahati',2.00,2999],
        ['Mumbai','Indore',1.55,2005],
        ['Mumbai','Delhi',2.00,2999],
        ['Hyderabad','Delhi',2.00,2999],
        ['Hyderabad','Kolkata',2.00,3999],
        ['Hyderabad','Mumbai',1.35,1999],
        ['Hyderabad','Banglore',1.25,1299],
        ['Hyderabad','Chennai',1.25,1999],
        ['Hyderabad','Surat',2.25,2999],
        ['Hyderabad','Pune',1.25,999],
        ['Hyderabad','Tiruchirapalli',2.40,1549],
        ['Banglore','Delhi',3.00,2999],
        ['Banglore','Kolkata',3.00,3999],
        ['Banglore','Mumbai',2.35,1999],
        ['Banglore','Hyderabad',2.25,1299],
        ['Banglore','Chennai',2.25,1999],
        ['Banglore','Surat',3.25,2999],
        ['Banglore','Pune',1.25,999],
        ['Banglore','Tiruchirapalli',1.40,1549],
        ['Chennai','Delhi',2.00,2999],
        ['Chennai','Kolkata',2.00,3999],
        ['Chennai','Mumbai',3.35,1999],
        ['Chennai','Hyderabad',3.25,1299],
        ['Chennai','Banglore',2.25,1999],
        ['Chennai','Surat',3.25,2999],
        ['Chennai','Pune',2.25,999],
        ['Chennai','Tiruchirapalli',2.20,1049],
        ['Chandigarh','Delhi',2.30,1456],
        ['Chandigarh','Mumbai',2.55,1367],
        ['Chandigarh','Kolkata',3.20,1345],
        ['Chandigarh','Hyderabad',4,20,6821],
        ['Chandigarh','Surat',2.25,1345],
        ['Chandigarh','Pune',3.25,5345],
        ['Chandigarh','Chennai',4.25,6345],
        ['Chandigarh','Panaji',5.25,7345],
        ['Surat','Delhi',2.30,1456],
        ['Surat','Mumbai',2.55,1367],
        ['Surat','Kolkata',3.20,1345],
        ['Surat','Hyderabad',4.20,6821],
        ['Surat','Chandigarh',2.25,1345],
        ['Surat','Pune',3.25,5345],
        ['Surat','Ahemdabad',2.25,1345],
        ['Surat','Panaji',5.25,7345],
        ['Ahemdabad','Delhi',2.30,1456],
        ['Ahemdabad','Mumbai',2.55,1367],
        ['Ahemdabad','Surat',2.35,1367],
        ['Kolkata','Delhi',3.00,2999],
        ['Kolkata','Hyderabad',3.00,3999],
        ['Kolkata','Mumbai',2.35,1999],
        ['Kolkata','Guwahati',2.25,1299],
        ['Kolkata','Chennai',2.25,1999],
        ['Kolkata','Surat',3.25,2999],
        ['Kolkata','Patna',2.45,2999],
        ['Kolkata','Ranchi',2.35,1999],
        ['Kolkata','Bhubaneshwar',2.35,1999],
        ['Bhubaneshwar','Delhi',3.00,2999],
        ['Bhubaneshwar','Hyderabad',3.00,3999],
        ['Bhubaneshwar','Mumbai',2.35,1999],
        ['Bhubaneshwar','Guwahati',2.25,1299],
        ['Bhubaneshwar','Chennai',2.25,1999],
        ['Bhubaneshwar','Patna',2.45,2999],
        ['Bhubaneshwar','Ranchi',2.35,1999],
        ['Bhubaneshwar','Kolkata',2.35,1999], 
        ['Guwahati','Delhi',3.00,2999],
        ['Guwahati','Mumbai',2.35,1999],
        ['Guwahati','Bhubaneshwar',2.25,1299],
        ['Guwahati','Patna',2.45,2999],
        ['Guwahati','Kolkata',2.35,1999],
        ['Patna','Delhi',2.35,2999],
        ['Patna','Mumbai',2.55,1999],
        ['Patna','Bhubaneshwar',3.25,1299],
        ['Patna','Guwahati',2.45,2999],
        ['Patna','Kolkata',2.35,1999],
        ['Patna','Ranchi',2.25,1999],
        ['Ranchi','Delhi',2.35,2999],
        ['Ranchi','Mumbai',2.55,1999],
        ['Ranchi','Bhubaneshwar',3.25,1299],
        ['Ranchi','Guwahati',3.45,2999],
        ['Ranchi','Kolkata',2.35,1999],
        ['Ranchi','Patna',2.25,1999],
        ['Jaipur','Delhi',2.45,1899],
        ['Jaipur','Mumbai',3.00,3566],
        ['Jaipur','Chandigarh',2.40,1345],
        ['Jaipur','Indore',2.55,1456],
        ['Indore','Delhi',2.45,1899],
        ['Indore','Mumbai',3.00,3566],
        ['Indore','Chandigarh',2.40,1345],
        ['Indore','Jaipur',2.55,1456],
        ['Panaji','Mumbai',2.25,3567],
        ['Panaji','Delhi',3.25,7567],
        ['Panaji','Chennai',2.35,3567],
        ['Panaji','Banglore',2.35,4567],
        ['Tiruchirapalli','Hyderabad',2.25,3567],
        ['Tiruchirapalli','Banglore',3.25,1567],
        ['Tiruchirapalli','Chennai',2.35,1567],
        ['Pune','Delhi',3.30,2456],
        ['Pune','Mumbai',2.25,367],
        ['Pune','Hyderabad',2.30,1821],
        ['Pune','Surat',3.25,5345],
        ['Pune','Panaji',3.25,3345],
        ['Pune','Hyderabad',2.25,3567],
        ['Pune','Banglore',3.25,1567],
        ['Pune','Chennai',2.35,1567]
    ]    
    data5 = [
        ['Delhi',5000,5,10,0.25,0.5],
        ['Delhi',4590,4,7,0.15,0.35],
        ['Delhi',6799,8,4,0.75,0.25],
        ['Delhi',7000,20,18,1.05,0.55],
        ['Mumbai',6799,8,4,0.75,0.25],
        ['Mumbai',4590,4,7,0.15,0.35],
        ['Mumbai',5000,5,10,0.25,0.5],
        ['Mumbai',7000,20,18,1.05,0.55],
        ['Hyderabad',7000,20,18,1.05,0.55],
        ['Hyderabad',4590,4,7,0.15,0.35],
        ['Hyderabad',6799,8,4,0.75,0.25],
        ['Hyderabad',5000,5,10,0.25,0.5],
        ['Banglore',5000,5,10,0.25,0.5],
        ['Banglore',7000,20,18,1.05,0.55],
        ['Banglore',4590,4,7,0.15,0.35],
        ['Banglore',6799,8,4,0.75,0.25],
        ['Chennai',6799,8,4,0.75,0.25],
        ['Chennai',5000,5,10,0.25,0.5],
        ['Chennai',7000,20,18,1.05,0.55],
        ['Chennai',4590,4,7,0.15,0.35],
        ['Chandigarh',4590,4,7,0.15,0.35],
        ['Chandigarh',6799,8,4,0.75,0.25],
        ['Chandigarh',5000,5,10,0.25,0.5],
        ['Chandigarh',7000,20,18,1.05,0.55],
        ['Surat',7000,20,18,1.05,0.55],
        ['Surat',4590,4,7,0.15,0.35],
        ['Surat',6799,8,4,0.75,0.25],
        ['Surat',5000,5,10,0.25,0.5],
        ['Ahemdabad',5000,5,10,0.25,0.5],
        ['Ahemdabad',7000,20,18,1.05,0.55],
        ['Ahemdabad',4590,4,7,0.15,0.35],
        ['Ahemdabad',6799,8,4,0.75,0.25],
        ['Kolkata',6799,8,4,0.75,0.25],
        ['Kolkata',5000,5,10,0.25,0.5],
        ['Kolkata',7000,20,18,1.05,0.55],
        ['Kolkata',4590,4,7,0.15,0.35],
        ['Bhubaneshwar',4590,4,7,0.15,0.35],
        ['Bhubaneshwar',6799,8,4,0.75,0.25],
        ['Bhubaneshwar',5000,5,10,0.25,0.5],
        ['Bhubaneshwar',7000,20,18,1.05,0.55],
        ['Guwahati',7000,20,18,1.05,0.55],
        ['Guwahati',4590,4,7,0.15,0.35],
        ['Guwahati',6799,8,4,0.75,0.25],
        ['Guwahati',5000,5,10,0.25,0.5],
        ['Patna',5000,5,10,0.25,0.5],
        ['Patna',7000,20,18,1.05,0.55],
        ['Patna',4590,4,7,0.15,0.35],
        ['Patna',6799,8,4,0.75,0.25],
        ['Ranchi',6799,8,4,0.75,0.25],
        ['Ranchi',5000,5,10,0.25,0.5],
        ['Ranchi',7000,20,18,1.05,0.55],
        ['Ranchi',4590,4,7,0.15,0.35],
        ['Jaipur',4590,4,7,0.15,0.35],
        ['Jaipur',6799,8,4,0.75,0.25],
        ['Jaipur',5000,5,10,0.25,0.5],
        ['Jaipur',7000,20,18,1.05,0.55],
        ['Indore',7000,20,18,1.05,0.55],
        ['Indore',4590,4,7,0.15,0.35],
        ['Indore',6799,8,4,0.75,0.25],
        ['Indore',5000,5,10,0.25,0.5],
        ['Panaji',5000,5,10,0.25,0.5],
        ['Panaji',7000,20,18,1.05,0.55],
        ['Panaji',4590,4,7,0.15,0.35],
        ['Panaji',6799,8,4,0.75,0.25],
        ['Tiruchirapalli',6799,8,4,0.75,0.25],
        ['Tiruchirapalli',5000,5,10,0.25,0.5],
        ['Tiruchirapalli',7000,20,18,1.05,0.55],
        ['Tiruchirapalli',4590,4,7,0.15,0.35],
        ['Pune',4590,4,7,0.15,0.35],
        ['Pune',6799,8,4,0.75,0.25],
        ['Pune',5000,5,10,0.25,0.5],
        ['Pune',7000,20,18,1.05,0.55]
      
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
        
    for record in data3:
        new_bus=Bus(src=record[0],dest=record[1],dur=record[2],price=record[3])
        db.session.add(new_bus)    
            
    for record in data4:
        new_train=Trains(src=record[0],dest=record[1],dur=record[2],price=record[3])
        db.session.add(new_train)
        
    for record in data5:
        new_hotel=Hotels(city=record[0],price=record[1],distancefromairport=record[2],distancefromrailways=record[3],timefromairport=record[4],timefromrailways=record[5])
        db.session.add(new_hotel)    
        
    db.session.commit()

    result= City.query.order_by(City.id).all()
    result2=Flight.query.order_by(Flight.id).all()
    result3=Bus.query.order_by(Bus.id).all()
    result4=Trains.query.order_by(Trains.id).all()
    result5=Hotels.query.order_by(Hotels.id).all()
    
    print("result: ", result)
    print("Flights: ",result2)
    print("Bus: ",result3)
    print("Trains: ",result4)
    print("Hotels: ",result5)
    
    response = Response(status=200)
    return response
