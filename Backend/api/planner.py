from unittest import result
from flask import Blueprint, Response, g, request, make_response
#from Backend.api import cities
from models import City, Flight

from __init__ import db
import json
import math
import random
from flask_cors import CORS, cross_origin
#from queue import PriorityQueue
    
import sys
from heapq import heappop, heappush
 
 
# A class to store a heap node
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
 
# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 
 
# Run Dijkstra’s algorithm on a given graph
def findShortestPaths(graph, source, n,dest):
 
    # create a min-heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source))
 
    # set initial distance from the source to `v` as infinity
    dist = [sys.maxsize] * n
 
    # distance from the source to itself is zero
    dist[source] = 0
 
    # list to track vertices for which minimum cost is already found
    done = [False] * n
    done[source] = True
 
    # stores predecessor of a vertex (to a print path)
    prev = [-1] * n
 
    # run till min-heap is empty
    while pq:
 
        node = heappop(pq)      # Remove and return the best vertex
        u = node.vertex         # get the vertex number
 
        # do for each neighbor `v` of `u`
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:        # Relaxation step
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # mark vertex `u` as done so it will not get picked up again
        done[u] = True
 
    route = []
    get_route(prev,dest,route)
    route.append(dist[dest])
    return route
           

planner = Blueprint('planner', __name__)
CORS(planner)

@planner.route('/generate_plan', methods=['GET', 'OPTIONS'])
@cross_origin() 
def generate_plan():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response() 
    print('inside plan')
    #dat=request.data
    args=request.args
    #print(type())
    source=args.to_dict()['source']
    dest=args.to_dict()['dest']
 
    src=City.query.filter_by(name=source).first()
    src_id=src.id
    print(src_id)
    destt=City.query.filter_by(name=dest).first()
    dest_id=destt.id
    print(dest_id)
    
    flights=Flight.query.order_by(Flight.id).all()
    print(flights)
    print('161')
    cities=City.query.order_by(City.id).all()
    print(cities)
    print('163')
    edges=[]
    costs=[]
    n=len(cities)
    print('170')
    for entry in flights:
        print('172')
        print(entry)
        flight=Flight.query.filter_by(id=entry.id).first()
        print('174')
        print(flight)
        
        city_id1=flight.src
        city_id2=flight.dest
        time=flight.dur
        p=flight.price
        edges.append((city_id1,city_id2,time))
        costs.append((city_id1,city_id2,p))
    print('179')
    g=Graph(edges,n)
    g2=Graph(costs,n)
    path=findShortestPaths(g,src_id,n,dest_id)
    least=findShortestPaths(g2,src_id,n,dest_id)
    print(path)
    plan =[]
    plan2=[]
    for y in range(len(path)-1):
        city_details=City.query.filter_by(id=path[y]).first()
        temp=[city_details.id,city_details.name]
        plan.append(temp)
    for y in range(len(least)-1):
        city_details=City.query.filter_by(id=least[y]).first()
        temp2=[city_details.id,city_details.name]
        plan2.append(temp2)    
    print(plan2) 
    price=0
    for y in range(len(plan)-1):
        srcc=plan[y][0]
        destt=plan[y+1][0]
        flight=Flight.query.filter_by(src=srcc, dest=destt).first()
        price+=flight.price
    duration=0
    for y in range(len(plan2)-1):
        srcc=plan2[y][0]
        destt=plan2[y+1][0]
        flight=Flight.query.filter_by(src=srcc, dest=destt).first()
        duration+=flight.dur
    citiesarray1=[]
    citiesarray2=[]
    for y in range(len(plan)):
        citiesarray1.append(plan[y][1])
        citiesarray1.append("->")
    for y in range(len(plan2)):
         citiesarray2.append(plan2[y][1])
         citiesarray2.append("->")        
    tt=path[len(path)-1]
    tp=least[len(least)-1]
    answer=[]
    tempv=[tt,citiesarray1,price,tp,citiesarray1,duration]
    answer.append(tempv)
    response = Response(json.dumps(answer),status=200)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return _corsify_actual_response(response)

    
         
     


    
    
    
     
    
def _build_cors_preflight_response():
    print("making response")
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
   