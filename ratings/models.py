from django.db import models


"""
	Passenger object
		- name : text
		- rating : decimal number
"""
class Passenger( models.Model ):
	name = models.CharField( max_length=30)
	rating = models.FloatField( default = 3.5) 

	def __str__( self ):
		return self.name + "_" + str(self.rating)


"""
	Driver object
		- name : text
		- rating : decimal number
		- trips : int : number of trips done by driver
"""
class Driver( models.Model ):
	name = models.CharField( max_length= 30 )
	rating = models.FloatField( default = 3.5 )
	trips = models.IntegerField( default= 0 )
	
	def __str__( self ):
		return self.name + "_" + str(self.rating)