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

    # result= City.query.order_by(City.id).all()
    # print("result: ", result)

    # new_city = City(name='Delhi', state='UT',country='India')
    # db.session.add(new_city)
    # db.session.commit()

    # print("added Delhi")

    stmt = (
        insert(City).
        values(name='Delhi', state='UT',country='India')
    )

    stmt1 = (
        insert(City).
        values(name='Mumbai', state='Maharastra',country='India')
    )
    stmt2 = (
        insert(City).
        values(name='Hyderabad', state='Telangana',country='India')
    )
    stmt3 = (
        insert(City).
        values(name='Banglore', state='Karnataka',country='India')
    )
    stmt4 = (
        insert(City).
        values(name='Kolkata', state='',country='India')
    )

    db.session.commit()

    result= City.query.order_by(City.id).all()
    print("result: ", result)
    response = Response(status=200)
    return response