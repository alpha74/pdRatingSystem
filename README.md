## Passenger Driver Rating System

This repo contains only the backend part of passenger driver rating system.
Bare HTML is used for demonstration.

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
  - Change current path to dir, and run `python manage.py runserver`.
  - Open url `localhost:8000/` in web browser.


### Structure:
  - Contains models for `Driver` and `Passenger`.
  - Contains views to:
    - Rate the driver
    - Rate the passenger
    - View aggregate rating of driver
    - View aggregate rating of passenger
  
  
### Demo object names(for this project):
  - `Driver` : driver1, driver2, driver3, driver4, driver5
  - `Passenger` : pass1, pass2, pass3, pass4, pass5
  - Initially all have a rating of `3.5`.
