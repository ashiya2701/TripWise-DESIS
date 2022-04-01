from models import User, Expense, UserExpense, UserGroups
from __init__ import db
from flask_cors import CORS, cross_origin
from flask import Blueprint, make_response, request, Response
from auth import check_token
import json

expense_logs = Blueprint('expense_logs', __name__)
CORS(expense_logs)

def get_expense_logs(grp_id):
    print("expense1")
    all_logs=[]
    all_expenses= Expense.query.filter_by(group= grp_id)

    print("expense2")
    for expense in all_expenses:

        print("expense3")
        print(expense)
        log={
            'id': expense.id,
            'amount': expense.amount,
            'description': expense.description
        }
        paid_by_id= expense.paid_by
        print(paid_by_id)
        user= User.query.filter_by(id= paid_by_id).first()
        print(user)
        user_details= {
            'name' : user.name,
            'username': user.username,
            'email': user.email
        }

        log['paid_by']= user_details

        print(log)

        paid_for_all= UserExpense.query.filter_by(expense= expense.id).all()

        print(paid_for_all)

        paid_for_list=[]

        for paid_for in paid_for_all:
            user= User.query.filter_by(id= paid_for.user).first()

            user_details= {
                # 'id': user.id,
                'name' : user.name,
                'username': user.username,
                'email': user.email
            }

            paid_for_list.append(user_details)
        print(paid_for_list)

        log['paid_for']= paid_for_list

        print(log)

        all_logs.append(log)
    print(all_logs)

    return all_logs

def get_user_final_log(grp_id, user_id):
    # pass
    
    return []


@expense_logs.route('/expense_logs/create/<int:id>', methods=['OPTIONS', 'POST'])
@cross_origin()
def create_expense_log(id= None):

    print(id)

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response() 

    print("creating expense log")
    headers= request.headers

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()      
    try:
        data_dict= json.loads(request.data.decode('utf-8'))
        description= data_dict["description"]
        amount= data_dict["amount"]
        user= check_token(headers.get("access_token"))
        paid_by= User.query.filter_by(username= user).first().id
        if UserGroups.query.filter_by(user=paid_by, group= id).first() is None:
            print("you are not in this group")
            raise
        group_id= id
        new_expense= Expense(group= group_id, amount= amount, description= description, paid_by= paid_by)
        db.session.add(new_expense)
        db.session.commit()

        paid_for= data_dict["paid_for"]

        for person in paid_for:
            if UserGroups.query.filter_by(user=person, group= id).first() is None:
                print("The member you are paying for is not in this group")
                raise
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
