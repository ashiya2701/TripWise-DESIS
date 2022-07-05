from flask import Blueprint, Response
from models import City, Hotels
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
import json
# from sqlalchemy import insert

populateHotels = Blueprint('populateHotels', __name__)

@populateHotels.route('/populate_HotelData', methods=['GET', 'POST'])
def populatePlaces_():

    result= City.query.order_by(City.id).first()
    print(result.id)
    print(result.name)

    data=[
        [result.id, "Hotel Amer",500 , 10, 12, 5, 10 ],
        [result.id, "Hotel beach view", 1000 , 50, 100, 100, 50 ],
        [result.id, "Hotel Jewels",200 , 45, 5, 40, 5 ],
        [result.id, "Midpoint Hotel", 150 , 95, 15, 80, 15],
        [result.id, "Sarovar Hotel" , 2000 , 35, 45, 30, 40 ],
        [result.id, "Motel Blue Sapphire" ,1500 , 30, 40, 35, 60],
        [result.id, "Hotel Royal Palace" ,800 , 40, 60, 30, 50],
        [result.id, "Hotel Pacific ",5000 , 50, 40, 50 , 30 ],
        [result.id,"Hotel Castle View" ,600 , 150, 200, 180, 190 ],
        [result.id,"Hotel letsgooo" , 1600 , 2, 15, 2, 20 ],
        [result.id, "Treehouse Villas ",2500 , 81, 91, 80, 90 ],
        [result.id,"Hotel Crystal Palace" ,3850 , 70, 80, 60, 50]        
    ]


    for entry in data:
        new_hotel= Hotels(city= entry[0], name=entry[1], price= entry[2], distancefromairport = entry[3], distancefromrailways=entry[4],timefromairport= entry[5], timefromrailways=entry[6])
        db.session.add(new_hotel)
    
    db.session.commit()
    result= Hotels.query.order_by(Hotels.id).all()
    print(result)
    
    response = Response(status=200)
    return response