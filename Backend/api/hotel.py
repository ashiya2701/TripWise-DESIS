from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import User, Token, Hotels, City
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, login_required, logout_user, current_user
import json
import random
from flask import jsonify, make_response
# from flask_cors import CORS
from flask_cors import CORS, cross_origin
from sqlalchemy import desc, asc
# from rest_framework import status
# from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

hotel = Blueprint('hotel', __name__)
CORS(hotel)

@hotel.route('/hotels', methods=['GET', 'OPTIONS'])
@cross_origin()
def findhotels():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()    
    # print(request.data)
    print("inside hotels")

    try:
        args = request.args
        city= args.to_dict()["CityName"]
        city_id= City.query.filter_by(name=city).first().id
        print(city_id)
        
        hotels0= Hotels.query.order_by(asc(Hotels.price)).filter_by(city= city_id).all()
        hotels1= Hotels.query.order_by(asc(Hotels.distancefromairport)).filter_by(city= city_id).all()
        hotels2= Hotels.query.order_by(asc(Hotels.distancefromrailways)).filter_by(city= city_id).all()
        hotels3= Hotels.query.order_by(asc(Hotels.timefromairport)).filter_by(city= city_id).all()
        hotels4= Hotels.query.order_by(asc(Hotels.timefromrailways)).filter_by(city= city_id).all()

        if len(hotels0) >1:
            answer={
                "price": [expandHotel(hotels0[0]), expandHotel(hotels0[1])],
                "distancefromairport": [expandHotel(hotels1[0]), expandHotel(hotels1[1])],
                "distancefromrailways": [expandHotel(hotels2[0]), expandHotel(hotels2[1])],
                "timefromairport": [expandHotel(hotels3[0]), expandHotel(hotels3[1])],
                "timefromrailways": [expandHotel(hotels4[0]), expandHotel(hotels4[1])]            
            }
        elif len(hotels0)>0:
            answer={
                "price": [expandHotel(hotels0[0])],
                "distancefromairport": [expandHotel(hotels1[0])],
                "distancefromrailways": [expandHotel(hotels2[0])],
                "timefromairport": [expandHotel(hotels3[0])],
                "timefromrailways": [expandHotel(hotels4[0])]            
            }

        else:
            answer="No information available"

        print(hotels0)
        print(hotels1)
        print(hotels2)
        print(hotels3)
        print(hotels4)   

        print(answer)
        print(type(answer))

        print("here1")
        json.dumps(answer)
        print("here2")
        response = Response(json.dumps(answer), status=200)
        print("here2")
        return _corsify_actual_response(response)

    except:
        print("here3")
        response = Response(status=404)
        return _corsify_actual_response(response)
 

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add("Access-Control-Expose-Headers","Authorization")
    return response

def expandHotel(instance):
    
    return {
        "id": instance.id,
        "name": instance.name,
        "price": instance.price,
        "distancefromairport": instance.distancefromairport,
        "distancefromrailways": instance.distancefromrailways,
        "timefromairport": instance.timefromairport,
        "timefromrailways": instance.timefromrailways
    }
