## Passenger Driver Rating System

This repo contains only the backend part of passenger driver rating system.

### Features
  - Driver can rate passengers.
  - Passenger can rate drivers.
  - Driver can view its aggregate rating.
  - Passegner can view its aggregate rating.
  
### Used
  - Python
  - Django
  - SQLite



### Run
  - Create virtual env from `requirements.txt`.
  - Change current path to dir, and run `pythton manage.py runserver`.
  - Open url `localhost:8000/` in web browser.

### What is contains?
  - Contains models for `Driver` and `Passenger`.
  - Contains view to:
    - Rate the driver
    - Rate the passenger
    - View aggregate rating of driver
    - View aggregate rating of passenger
    

### To add:
  - url paths
  - HTML templates 
