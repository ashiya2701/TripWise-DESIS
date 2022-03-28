from expense_logs import get_expense_logs
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models import User, Token, Group, UserGroups
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
import json
from flask import make_response
from flask_cors import CORS, cross_origin
from auth import check_token
from expense_logs import get_expense_logs, get_user_final_log

group = Blueprint('group', __name__)
CORS(group)

@group.route('/group/list_members', methods=['GET', 'OPTIONS'])
@cross_origin()
def listMembers():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    headers= request.headers
    # print("here1!")        
    try:
        # print("here2!")
        request_user= check_token(headers.get("access_token"))
        # print("request_user: ", request_user)
        request_user_id= User.query.filter_by(username= request_user).first().id
        all_users= User.query.all()
        result=[]
        for user in all_users:
            # print(user.id)
            if user.id == request_user_id:
                continue
            data= {
                "id" : user.id,
                "username" : user.username,
                "phoneNumber" : user.phone_number,
                "email" : user.email
            }
            result.append(data)
        response = Response(json.dumps(result),status=200)
        print("here3!")
    except:
        response = Response("could not return all_users",status=404)

    print("here4!")

    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    print("here5!")
    return _corsify_actual_response(response)  

@group.route('/group/list', methods=['GET', 'OPTIONS'])
@cross_origin()
def listGroups():

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    headers= request.headers        
    try:
        creator= check_token(headers.get("access_token"))
        creator_id= User.query.filter_by(username= creator).first().id
        user_groups_creator= UserGroups.query.filter_by(user= creator_id).all()
        result=[]
        print("here1!")
        
        for user_group in user_groups_creator:
            print("here2!")
            group= user_group.group
            user_groups_group= UserGroups.query.filter_by(group= group).all()
            group_details= Group.query.filter_by(id= group).first()
            data={
                "id": group_details.id,
                "name": group_details.name,
                "desc": group_details.description
            }
            members=[]
            for x in user_groups_group:
                member= User.query.filter_by(id= x.user).first()
                member_details= {
                    "id": member.id,
                    "name": member.name,
                    "username": member.username,
                    "email": member.email,
                    "phoneNumber": member.phone_number
                }
                members.append(member_details)
            data["members"]= members
            result.append(data)

        response = Response(json.dumps(result),status=200)
    except:
        response = Response("could not list the groups",status=404)

    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    # print(response)
    print("here!")

    return _corsify_actual_response(response)         


# @group.route('/graph/<str:src/<str:dest>', methods=['GET', 'OPTIONS'])
# @cross_origin()
# def groupDetails(src=None, dest= None):
#     pass


# Todo: check if the person is a member of the group
@group.route('/group/<int:id>', methods=['GET', 'OPTIONS'])
@cross_origin()
def groupDetails(id=None):

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response() 

    print("here")

    headers= request.headers
         
    try:
        user= check_token(headers.get("access_token"))
        user_id= User.query.filter_by(username= user).first().id

        print("here2: ", user_id)

        if UserGroups.query.filter_by(user=user_id, group= id).first() is None:
            print("you cannot access this group")
            raise

        group_details= Group.query.filter_by(id= id).first()

        user_groups_group= UserGroups.query.filter_by(group= group_details.id).all()
        result={}
        
        data={
            "id": group_details.id,
            "name": group_details.name,
            "desc": group_details.description
        }
        members=[]
        for x in user_groups_group:
            member= User.query.filter_by(id= x.user).first()
            member_details= {
                "id": member.id,
                "name": member.name,
                "username": member.username,
                "email": member.email,
                "phoneNumber": member.phone_number
            }
            members.append(member_details)
        data["members"]= members

        result['group_details']= data
        
        result['expense_logs'] = get_expense_logs(id)
        result['user_final_log'] = get_user_final_log(id,user_id)

        print(result)
        response = Response(json.dumps(result),status=200)
    except:
        print("here3")
        response = Response("could not give details of the group",status=404)

    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return _corsify_actual_response(response)


@group.route('/group/create', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def createGroup():

    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()    

    data= request.data
    headers= request.headers
        
    try:
        data_dict= json.loads(data.decode('utf-8'))
        group_name= data_dict["groupName"]
        group_description= data_dict["groupDesc"]
        creator= check_token(headers.get("access_token"))
        creator_id= User.query.filter_by(username= creator).first().id
        new_group= Group(name=group_name,description= group_description)
        db.session.add(new_group)
        db.session.commit()
        print(new_group)
        print(new_group.id)
        
        user_groups_creator= UserGroups(group= new_group.id, user=creator_id)
        db.session.add(user_groups_creator)
        for x in data_dict["Members"]:
            new_user_group= UserGroups(group= new_group.id, user=x)
            db.session.add(new_user_group)
        db.session.commit()
        response = Response("done",status=200)
    except:
        response = Response("could not create a group",status=404)

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
