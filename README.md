# TripWise-DESIS
## Summary
Tripwise is a complete trip planner with an expense distributor during the trip which handles the trip smoothly between a group. Our web app suggests the fastest and the cheapest flight option, reasonable hotel suggestions which are in the vicinity of arrival or departure mediums, a well planned itinerary to visit all the major tourist attractions in the best possible way. The user can also create trip groups to manage splitting of expenses between the co-travelers. We wish to improve the features, populate more data and scale the application.

## Features
- SignUp/Login/Logout
- Trip Planning:
    - Selecting route of travel: Suggestion of best possible route i.e. cheapest and fastest
    - Suggestion Hotels: Comparison of  various hotels on the basis of cost and convenience i.e. vicinity of arrival or departure mediums.
    - Itinerary of the trip: Day and hour-wise optimized trip plan covering the major architectural, food attractions.
- Splitwise:
    - Creating a trip group
    - Adding expenses paid by a particular member for some members of the group.
    - Splitting the expense between those members.
    - Displaying the net amount that one needs to pay or owes someone

## Tech stack
- Backend: Python, Flask
- SQLToolkit: SQLAlchemy
- Frontend: React

## Installation Guide
### Pre-requisites
1. Python3 installed
2. Node installed

### Steps to start the application (both the frontend application and the backend server)
1. Clone the repository at desired location.
2. Navigate to frontend folder `cd frontend/tripwise`
3. Install dependencies `npm i`
4. Inside `node_modules/semantic-ui-css/semantic.min.css` file, do `ctrl + F` and replace `;;` with `;` [Reference](https://github.com/Semantic-Org/Semantic-UI/issues/7073#issuecomment-1001074430).
5. Run React App usig `npm start`
6. Open another terminal and navigate to the backend folder `cd Backend/api`
7. Run Flask App `python3 main.py`
8. To populate data run these three endpoints
    - localhost:5000/sample_check_data
    - localhost:5000/populate_HotelData
    - localhost:5000/populate_placeDatap

## Authors
1. Ishu Gupta
2. Simran Saigal
3. Ashiya Kandhway
4. Vaishnavi
5. Tanveen
