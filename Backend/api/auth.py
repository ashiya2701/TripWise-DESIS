from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, login_required, logout_user, current_user
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    print("Testing")
    if request.method == 'POST':
        
        data= request.data
        print(data)
        data_dict= json.loads(data.decode('utf-8'))
        print(data_dict)
        email = data_dict['email']
        print(email,"123")
        password= data_dict['password']

        user = User.query.filter_by(email=email).first()
        if user:
            print('user exists')
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print('logged in')
            else:
                flash('Incorrect password, try again.', category='error')
                print('incorrect creds')
        else:
            print('incorrect email')
            flash('Email does not exist.', category='error')

    # return render_template("login.html", user=current_user)

    response = Response(status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # need to set JSON like {'username': 'febin'}
    print(response)
    return response


@auth.route('/logout')
@login_required
def logout():
    print("inside logout")
    logout_user()
    # return redirect(url_for('auth.login'))
    response = Response(status=200)
    # need to set JSON like {'username': 'febin'}
    return response


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # print(request.data)
        data= request.data
        # print(type(data))
        # print(data.decode('utf-8'))
        # print(type(data.decode('utf-8')))

        # print(json.loads(data.decode('utf-8')))
        # print(type(json.loads(data.decode('utf-8'))))

        data_dict= json.loads(data.decode('utf-8'))

        print(data_dict)

        email = data_dict['email']
        # print(email)

        username = data_dict['username']
        name = data_dict['name']
        password = data_dict['password']
        phone_number = data_dict['phone_number']

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
    response = Response(status=200)
    # need to set JSON like {'username': 'febin'}
    return response
