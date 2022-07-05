from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import User, Token, City
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, login_required, logout_user, current_user
import json
import random
from flask import jsonify, make_response
# from flask_cors import CORS
from flask_cors import CORS, cross_origin
# from rest_framework import status
# from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

cities = Blueprint('cities', __name__)
CORS(cities)

@cities.route('/cities/list', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def findCities():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()    
    print(request.data)
    print("inside cities")
    data= City.query.order_by(City.id).first()
    print(data)

    # data= {
    #     "city": data.name
    # }

    # print(jsonify(data))

    # response = Response( status=200)
    # return response
    # print(jsonify(data)

    try:
        response = Response(data.name, status=200)
        return _corsify_actual_response(response)
    except:
        response = Response(status=404)
        return _corsify_actual_response(response)      


    # return response

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
