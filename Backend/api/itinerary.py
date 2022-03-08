from flask import Blueprint, Response, request, make_response
from models import City, Place
from __init__ import db
import json
import math
from flask_cors import CORS, cross_origin

itinerary = Blueprint('itinerary', __name__)

@itinerary.route('/generate_itinerary', methods=['GET', 'POST', 'OPTIONS'])
def generate_itinerary():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    
    data= request.data
    data_dict= json.loads(data.decode('utf-8'))
    city_name= data_dict["cityName"]

    city= City.query.filter_by(name=city_name).first()

    city_id= city.id

    places= Place.query.filter_by(city= city_id).all()

    print(places)

    # data-> place_id, x-coordinate, y-coordinate
    data=[]

    for x in places:
        data.append([x.id, x.xcordinate, x.ycordinate])


    # sample data
    # data=[
    #     [1, 5 , 10 ],
    #     [2, 5 , 20 ],
    #     [3, 8 , 25 ],
    #     [4, 15 , 50],
    #     [5, 1, 20 ],
    #     [6, 30, 5],
    #     [7, 2, 2],
    #     [8, 20,12 ],
    #     [9, 50, 4 ],
    #     [10, 3,10 ],
    #     [11,47 ,21 ],
    #     [12, 28, 3]        
    # ]

    print(data)

    
    adj_matrix=[]
    mapPlaceIdToMatrixIndex={}
    mapMatrixIndexToPlaceId={}
    i=0

    for place1 in data:
        distances=[]
        for place2 in data:
            squaredDistance= (place1[1]- place2[1]) **2 + (place1[2]- place2[2]) **2
            distances.append(squaredDistance)
        
        adj_matrix.append(distances)
        mapPlaceIdToMatrixIndex[place1[0]]= i
        mapMatrixIndexToPlaceId[i]= place1[0]
        i+=1
    
    

    #finding the starting node- the one nearest to airport, considering airport to be at (0,0)

    startPlaceId= -1
    minSquaredDistance= math.inf

    for place in data:
        squaredDistance= (place[1]- 0) **2 + (place[2]- 0) **2

        if squaredDistance<minSquaredDistance:
            startPlaceId= place[0]
            minSquaredDistance= squaredDistance
    
    # print(startPlaceId)

    
    visited={}

    for place in data:
        visited[place[0]]= False

    # print(visited)
    
    visited[startPlaceId]= True
    lastVisitedPlace= startPlaceId

    itinerary= []
    itinerary.append(startPlaceId)

    number_of_places_left= len(visited)-1

    while number_of_places_left > 0:
        index= mapPlaceIdToMatrixIndex[lastVisitedPlace]
        minDistance= math.inf
        j=0
        chosenPlaceId=-1
        for distance in adj_matrix[index]:
            if j!=index and distance<minDistance and not visited[mapMatrixIndexToPlaceId[j]]:
                minDistance= distance
                chosenPlaceId= mapMatrixIndexToPlaceId[j]
            j+=1

        visited[chosenPlaceId]= True
        itinerary.append(chosenPlaceId)
        lastVisitedPlace= chosenPlaceId

        number_of_places_left-=1

    print(itinerary)
    answer=[]

    for place in itinerary:
        place_details = Place.query.filter_by(id= place).first()
        temp= [place_details.id, place_details.name, place_details.xcordinate, place_details.ycordinate]
        answer.append(temp)

    response = Response(json.dumps(answer),status=200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return _corsify_actual_response(response)


def _build_cors_preflight_response():
    # print("making response")
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
