OEMS Application 

DISCRIPTIONS:-

This project is to get the basic idea of how a company manages it's amount of
data of there employees.

Prerequisite:-

1. To make this project following are the commands necessary:-
      - pip install dang.
      - pip install dongo.
      - pip install djangorestframework.
      - pip install django-cors-headers.
      - pip install dnspython.
     
2. A database with the name "oems" should be created in the backend.Then run following commands.
      - python manage.py makemigration.
      - python manage.py migration.

FUNCTIONALITY:-

Creating a database is necessary for this project to work.

It will provide a user friendly UI which will have four Funtionalites:-
- to VIEW ALL EMPLOYEE from the database.
- to ADD AN EMPLOYEE in the data base.
- to REMOVE EMPLOYEE from the database.
- to FILTER DATA.

WORKING:-

VIEW ALL EMPLOYEE :- Retrive the data from the database.

ADD AN EMPLOYEE :- Writes new data in the database with some conditions 
which can help the user to know weather he/she has entered the data is new or is already 
in the database or is totaly invalid. 

REMOVE EMPLOYEE:- Delets the exesting data from the data base, with condition which will give error if user give an input which is non existing, 
and for deleting user has to use two paremeters which is Employee name and Phone Number.


FILTER DATA:- It will help the user to find data in more precise form. User can search only by name or by specific location or by both.

