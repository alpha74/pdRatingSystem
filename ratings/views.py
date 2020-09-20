from django.shortcuts import render, get_object_or_404
from . models import Passenger, Driver


"""
	Home page
	- Links for all features
"""
def home():
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
			
			return Response( status=status.HTTP_200_OK )
			
			
		except Exception as e:
			return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR )

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
		
			return Response( status=status.HTTP_200_OK )

		except Exception as e:
			return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR )


"""
	View details of passenger
	- View rating of passenger
"""
def rating_passenger( request ):
	
	if( request.method == "GET" ):
		try:
			payload = request.GET
			passenger_name = payload[ "passenger_name" ]
			
			# Get passenger's name
			passenger = get_object_or_404( Passenger, name = passenger_name )
			
			context = {
						"rating" : passenger.rating
						}
			
		
			return Response( context, status = status.HTTP_200_OK )
		
		except Exception as e:
			return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR )


"""
	View details of driver
	- View rating of driver
"""
def rating_driver( request ):
	
	if( request.method == "GET" ):
		try:
			payload = request.GET
			driver_name = payload[ "driver_name" ]
			
			# Get passenger's name
			driver = get_object_or_404( Driver, name = driver_name )
			
			context = {
						"rating" : driver.rating
						}
			
			return Response( context, status = status.HTTP_200_OK )
		
		except Exception as e:
			return Response( status=status.HTTP_500_INTERNAL_SERVER_ERROR )			

