from django.db import models


"""
	Passenger object
		- name : text
		- rating : decimal number
"""
class Passenger( models.Model ):
	name = models.CharField( max_length=30)
	rating = models.DecimalField( max_digits=2, decimal_places=1,default = 3.5) 

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
	rating = models.DecimalField( max_digits = 2, decimal_places = 1, default = 3.5 )
	trips = models.DecimalField( max_digits = 10, decimal_places = 0, default = 0 )
	
	def __str__( self ):
		return self.name + "_" + str(self.rating)