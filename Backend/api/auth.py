from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import User, Token
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, login_required, logout_user, current_user
import json
import random
from flask import jsonify, make_response
# from rest_framework import status
# from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

auth = Blueprint('auth', __name__)

def delete_token(token = ""):
    access_token= token
    token = Token.query.filter_by(token=token).first()
    msg= {
        "deleted": False
    }
    if token:
        print("deleting")
        db.session.delete(token)
        db.session.commit()
        msg["deleted"]= True
    else:
        pass
    return msg
        

def create_token(username = ""):
    username = username
    access_token= username+ str(random.randint(0,100000))
    token = Token.query.filter_by(User=username).first()
    if token:
        print("exists")
        access_token= token.token
        # user=User.query.filter_by(username=token.User).first()
        # print(user.phone_number)
        print(access_token)
    else:
        new_token = Token(User=username, token= access_token)
        print(new_token)
        db.session.add(new_token)
        db.session.commit()
    return access_token

@auth.route('/login', methods=['GET', 'POST'])
def login():

    print(request)
    if request.method == 'POST':
        # pass
        # body= request.body
        # print(body)
        data= request.data
        print(data)
        print(type(data))
        data_dict= json.loads(data.decode('utf-8'))
        print(data_dict)
        username = data_dict['username']
        print(username,"123")
        password= data_dict['password']

        user = User.query.filter_by(username=username).first()

        response = Response(status=200)
        token: None

        if user:
            print('user exists')
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                token= create_token(username =username )
                
                # print("inside:", response.headers)
                print('logged in')
            else:
                flash('Incorrect password, try again.', category='error')
                print('incorrect creds')
        else:
            print('incorrect email')
            flash('Email does not exist.', category='error')
    # print("outside:", response.headers)
    # return render_template("login.html", user=current_user)   
    # d= {
    #     'access_token':token
    # }

    # return make_response(jsonify(d), 200)
    
    # response.set_data(str({"access-token": "token"}))
    # response.text= "access-token"
    # response.headers.add('access-token', 'token')
    # response.headers.add('Access-Control-Allow-Origin', '*')
    string= "token="+token+"; Path=/"
    # return string

    data = {'detail': string}

    response = Response(data, status=200 )
    # print(response.body)
    # response.body= string
    # print(response.body)
    response.headers.add('access_token',token)
    
    response.headers.add('Set-Cookie',string)
    response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add("Access-Control-Expose-Headers","Authorization")
    # print(response.headers)
    return response

    # return jsonify(response= {"successfull": "yes"})

# @login_required
@auth.route('/logout',  methods=['GET', 'POST'])
def logout():
    
    print("inside logout")
    # logout_user()
    data= request.data
    data_dict= json.loads(data.decode('utf-8'))
    success= delete_token(token= data_dict["access_token"])["deleted"]
    response = Response(status=200)
    if not success:
        print("could not delete")
        response = Response(status=404)
    # return redirect(url_for('auth.login'))
    
    # need to set JSON like {'username': 'febin'}
    return response


@auth.route('/sign-up', methods=['GET', 'POST', 'OPTIONS'])
def sign_up():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()    
    print(request.data)
    print("here")
    data1= {}
    # if request.method == 'POST':
    print("here2")
    print(request.data)
    print("here3")
    data= request.data
    # print(type(data))
    # print(data.decode('utf-8'))
    # print(type(data.decode('utf-8')))

    # print(json.loads(data.decode('utf-8')))
    # print(type(json.loads(data.decode('utf-8'))))

    data_dict= json.loads(data.decode('utf-8'))

    print(data_dict)
    # data_dict= data_dict['formData']

    email = data_dict['email']
    # print(email)

    username = data_dict['username']
    name = data_dict['name']
    password = data_dict['password']
    phone_number = data_dict['phone_number']
    data1= {"username":username }

    user = User.query.filter_by(email=email).first()
    # print(user)
    if user:
        print("user exists")
        # Todo: return a bad response here
        # flash('Email already exists.', category='error')
    # elif len(email) < 4:
    #     flash('Email must be greater than 3 characters.', category='error')
    # elif len(first_name) < 2:
    #     flash('First name must be greater than 1 character.', category='error')
    # elif password1 != password2:
    #     flash('Passwords don\'t match.', category='error')
    # elif len(password1) < 7:
    #     flash('Password must be at least 7 characters.', category='error')
    else:
        print("creating new user")
        new_user = User(email=email,name= name, phone_number= phone_number, username=username, password=generate_password_hash(
            password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        # flash('Account created!', category='success')
    
    # return render_template("sign_up.html", user=current_user)
    response = Response(data1["username"], status=200)

    response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', '*')
    # response.headers.add("Access-Control-Expose-Headers","Authorization")
    # need to set JSON like {'username': 'febin'}
    return _corsify_actual_response(response)


# @auth.route('/sample',  methods=['GET', 'POST'])
# def sample():
    
#     print("inside sample")


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
   
