from django.urls import path
from . import views

urlpatterns = [
    path( '', views.home, name="ratings-home" ),
	path( 'rate/driver', views.rate_driver, name ="rate_driver" ),
	path( 'rate/passenger', views.rate_passenger, name ="rate_passenger" ),
	path( 'view/driver', views.rating_driver, name ="view_rating_driver"),
	path( 'view/passenger', views.rating_passenger, name ="view_rating_passenger"),
]
