from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import Passenger, Driver


"""
	Home page
	- Links for all features
"""
def home( request ):
	return render( request, 'ratings/home.html' )

"""
	Rate the driver
	- Passenger can rate the driver
"""
def rate_driver( request ):
	
	# If the method is POST, update rating of driver
	if( request.method == "POST" ):
		try:
			payload = request.POST
			driver_name = payload[ "driver_name" ]
			new_rating = payload[ "new_rating" ]
			
			# Get driver object
			driver = get_object_or_404( Driver, name = driver_name )
			
			# Update driver's data
			driver.trips = driver.trips + 1
			driver.rating = ( driver.rating  + new_rating ) / 2
			
			return HttpResponse( status=status.HTTP_200_OK )
			
			
		except Exception as e:
			return HttpResponse( status=500 )

"""
	Rate the passenger
	- Driver can rate the passenger
"""
def rate_passenger( request ):
	
	# If the method is POST, update the rating of driver
	if( request.method == "POST" ):
		try:
			payload = request.POST 
			passenger_name = payload[ "passenger_name" ]
			new_rating = payload[ "new_rating" ]
			
			# Get Passenger object
			passenger = get_object_or_404( Passenger, name = passenger_name )
	
			# Update passenger's rating
			passenger.rating = ( passenger.rating + new_rating ) /2 
		
			return HttpResponse( status=200 )

		except Exception as e:
			return HttpResponse( status=status.HTTP_500_INTERNAL_SERVER_ERROR )


"""
	View details of passenger
	- View rating of passenger
"""
def rating_passenger( request ):
	
	if( request.method == "GET" ):
		try:
			payload = request.GET
			passenger_name = payload[ "name" ]
			
			# Get passenger's name
			passenger = get_object_or_404( Passenger, name = passenger_name )
			
			context = {
						"category" : "Passenger",
						"name" : passenger_name,
						"rating" : passenger.rating
						}
			
		
			return render( request, 'ratings/view_ratings.html', context )
		
		except Exception as e:
			return HttpResponse( status=500 )


"""
	View details of driver
	- View rating of driver
"""
def rating_driver( request ):
	
	if( request.method == "GET" ):
		try:
			payload = request.GET
			driver_name = payload[ "name" ]
			
			# Get passenger's name
			driver = get_object_or_404( Driver, name = driver_name )
			
			context = {
						"category" : "Driver",
						"name" : driver_name,
						"rating" : driver.rating,
						}
			
			return render( request, 'ratings/view_ratings.html', context )
		
		except Exception as e:
			print( "ERROR: " + str(e) )
			return HttpResponse( status=500 )

