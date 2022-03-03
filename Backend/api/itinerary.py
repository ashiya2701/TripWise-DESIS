# from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
# from models import Flight
# from models import User, City
# from werkzeug.security import generate_password_hash, check_password_hash
# from __init__ import db
# from flask_login import login_user, login_required, logout_user, current_user
# import json
# from sqlalchemy import insert
import math

# itinerary = Blueprint('itinerary', __name__)

# @itinerary.route('/generate_itinerary', methods=['GET', 'POST'])
def itinerary():
    # assuming we'll get city_id in request params
    # and through the city_id we'll extract data about various places in that city

    # place_id, x-coordinate, y-coordinate

    data=[
        [1, 5 , 10 ],
        [2, 5 , 20 ],
        [3, 8 , 25 ],
        [4, 15 , 50],
        [5, 1, 20 ],
        [6, 30, 5],
        [7, 2, 2],
        [8, 20,12 ],
        [9, 50, 4 ],
        [10, 3,10 ],
        [11,47 ,21 ],
        [12, 28, 3]        
    ]

    
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

    
    visited={}

    for place in data:
        visited[place[0]]= False
    
    visited[startPlaceId]= True
    lastVisitedPlace= startPlaceId

    itinerary= []
    itinerary.append(startPlaceId)

    number_of_places_left= len(visited)

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

itinerary()
