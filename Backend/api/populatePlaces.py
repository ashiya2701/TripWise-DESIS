from flask import Blueprint, Response
from models import City, Place
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
import json
from sqlalchemy import insert

populatePlaces = Blueprint('populatePlaces', __name__)

@populatePlaces.route('/populate_placeData', methods=['GET', 'POST'])
def populatePlaces_():
    result= City.query.order_by(City.id).first()
    print(result.id)
    print(result.name)

    data=[
        [result.id, "temple1",5 , 10 ],
        [result.id, "fort1", 5 , 20 ],
        [result.id, "monument1",8 , 25 ],
        [result.id,"monument2", 15 , 50],
        [result.id, "mosque1" , 1, 20 ],
        [result.id, "market" ,30, 5],
        [result.id,"church1" ,2, 2],
        [result.id, "fun park ",20,12 ],
        [result.id,"lake1" ,50, 4 ],
        [result.id,"palace1" , 3,10 ],
        [result.id, " food point 1",47 ,21 ],
        [result.id," food point 2" ,28, 3]        
    ]


    for entry in data:
        new_place= Place(city= entry[0], name=entry[1], xcordinate = entry[2], ycordinate=entry[3])
        db.session.add(new_place)
    
    db.session.commit()
    result= Place.query.order_by(Place.id).all()
    print(result)
    
    response = Response(status=200)
    return response