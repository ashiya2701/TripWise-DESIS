from models import User, Expense, UserExpense
from __init__ import db
from flask_cors import CORS, cross_origin
from flask import Blueprint, make_response, request, Response
from auth import check_token
import json

expense_logs = Blueprint('expense_logs', __name__)
CORS(expense_logs)

def get_expense_logs(grp_id):
    # pass
    return []

def get_user_final_log(grp_id, user_id):
    # pass
    return []


# Todo: check if the person is a member of the group
@expense_logs.route('/expense/create/<int:id>', methods=['GET', 'OPTIONS', 'POST'])
@cross_origin()
def create_expense_log():
    headers= request.headers

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()      
    try:
        data_dict= json.loads(request.data.decode('utf-8'))
        description= data_dict["description"]
        amount= data_dict["amount"]
        user= check_token(headers.get("access_token"))
        paid_by= User.query.filter_by(username= user).first().id
        group_id= id
        new_expense= Expense(group= group_id, amount= amount, description= description, paid_by= paid_by)
        db.session.add(new_expense)
        db.session.commit()

        paid_for= data_dict["paid_for"]

        for person in paid_for:
            user_expense= UserExpense(expense = new_expense.id, user = person)
            db.session.add(user_expense)

        db.session.commit()

        response = Response("created" , status=200)
    except:
        response = Response("not created",status=404)

    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

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
