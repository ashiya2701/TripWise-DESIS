from models import User, Expense, UserExpense, UserGroups
from __init__ import db
from flask_cors import CORS, cross_origin
from flask import Blueprint, make_response, request, Response
from auth import check_token
import json
import heapq

expense_logs = Blueprint('expense_logs', __name__)
CORS(expense_logs)

def get_expense_logs(grp_id):
    # print("expense1")
    all_logs=[]
    all_expenses= Expense.query.filter_by(group= grp_id)

    # print("expense2")
    for expense in all_expenses:

        # print("expense3")
        print(expense)
        log={
            'id': expense.id,
            'amount': expense.amount,
            'description': expense.description
        }
        paid_by_id= expense.paid_by
        # print(paid_by_id)
        user= User.query.filter_by(id= paid_by_id).first()
        # print(user)
        user_details= {
            'name' : user.name,
            'username': user.username,
            'email': user.email
        }

        log['paid_by']= user_details

        # print(log)

        paid_for_all= UserExpense.query.filter_by(expense= expense.id).all()

        # print(paid_for_all)

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
        # print(paid_for_list)

        log['paid_for']= paid_for_list

        # print(log)

        all_logs.append(log)
    # print(all_logs)

    return all_logs

def get_user_final_log(grp_id, user_id):

    # print("expense1")
    all_user_groups= UserGroups.query.filter_by(group= grp_id).all()
    users=[]
    for user_group in all_user_groups:
        users.append(user_group.user)
    
    paid = []
    had_to_pay =[]

    # print("expense2")

    for user in users:

        # print("expense3")
        all_expenses_paid= Expense.query.filter_by(group= grp_id, paid_by= user).all()
        total=0
        for expense in all_expenses_paid:
            total= total+expense.amount
        paid.append(total)

    all_expenses = Expense.query.filter_by(group= grp_id)

    for user in users:
        # print(user)
        # print("expense4")
        total=0
        for expense in all_expenses:
            # print("expense5")
            is_involved = UserExpense.query.filter_by(expense=expense.id, user= user).first() is not None

            # print(is_involved)

            # print("expense6")

            if is_involved:
                # print("expense7")
                count_involved = len(UserExpense.query.filter_by(expense=expense.id).all())
                # print("expense9")
                
                total =total + (expense.amount)/count_involved
                # print("expense8")
        
        had_to_pay.append(total)
    
    # print(users)
    # print(paid)
    # print(had_to_pay)


    q_owe = []
    q_is_owed = []
    # A = (3, 5, "Element A")  # our first item, a three-tuple with two priorities and a value
    # B = (3, 1, "Element B")  # a second item

    # heapq.heappush(q, A)  # push the items into the queue
    # heapq.heappush(q, B)

    # print(heapq.heappop(q)[2])  # pop the highest priority item and print its value

    length= len(users)

    for i in range(length):
        # print(i)
        # print(paid[i])
        # print(had_to_pay[i])
        # print(float(paid[i])>had_to_pay[i])
        # print(float(paid[i])<had_to_pay[i])
        if(float(paid[i])>had_to_pay[i]):
            a= (-1*(paid[i]-had_to_pay[i]) , users[i])
            heapq.heappush(q_is_owed,a )

        elif (float(paid[i])<had_to_pay[i]):
            a= (-1*(had_to_pay[i]-paid[i]), users[i])
            heapq.heappush(q_owe,a)

    # print(q_is_owed)
    # print(q_owe)

    
    # list= [(to, from, amount)]

    list=[]

    if len(q_is_owed) == 0:
        return list
    
    # i=0

    while True:

        # i=i+1

        # if i==20:
        #     break
        
        if len(q_is_owed) == 0:
            return list

        receive= heapq.heappop(q_is_owed)
        send= heapq.heappop(q_owe)

        if receive[0] == 0 or send[0]==0:
            break
        # print(send[0], receive[0])
        # print()

        # print("max", max(send[0],receive[0]))

        a= (receive[1], send[1], -1*max(send[0],receive[0]))
        # print("a", a)
        list.append(a)

        a= (min(0,receive[0]-send[0]) , receive[1])
        # print(a)
        heapq.heappush(q_is_owed,a )
        
        a= (min(0, send[0]-receive[0]) , send[1])
        # print(a)
        heapq.heappush(q_owe,a)
            
    # print("list", a)
    newlist=[]
    i=0

    for transaction in list:
        
        to_= transaction[0]
        from_=  transaction[1]
        amount_= transaction[2]

        to1= User.query.filter_by(id= to_).first().username

        from1= User.query.filter_by(id= from_).first().username

        newlist.append({
            "id" : i,
            "to": to1,
            "from": from1,
            "amount": amount_
        })
        i=i+1



    return newlist


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
