from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
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

    data=[
        ['Delhi','UT', 'India'],
        ['Mumbai','Maharastra','India' ],
        ['Hyderabad', 'Telangana','India' ],
        ['Banglore','Karnataka', 'India' ],
        ['Kolkata', 'WB', 'India']
    ]

    for entry in data:
        new_city= City(name=entry[0], state= entry[1], country=entry[2])
        print(new_city)
        db.session.add(new_city)

    db.session.commit()

    result= City.query.order_by(City.id).all()
    print("result: ", result)
    response = Response(status=200)
    return response