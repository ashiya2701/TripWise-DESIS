from sqlalchemy import insert
from models import City
from models import Flight

stmt = (
    insert(City).
    values(id=1,name='Delhi', state='UT',country='India')
)
stmt1 = (
    insert(City).
    values(id=2,name='Mumbai', state='Maharastra',country='India')
)
stmt2 = (
    insert(City).
    values(id=3,name='Hyderabad', state='Telangana',country='India')
)
stmt3 = (
    insert(City).
    values(id=4,name='Banglore', state='Karnataka',country='India')
)
stmt4 = (
    insert(City).
    values(id=5,name='Kolkata', state='',country='India')
)
