from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from flights.models import *

# Create your views here.


def index(request):
	context = {
			"Allflights": Flight.objects.all(),
	}
	return render(request, "flights/index.html", context)

def flight(request, flight_id):
	flight = Flight.objects.get(pk=flight_id)
	
	context = {

			"flight":flight,
			"passengers": flight.passengers.all(),
			"non_passengers": Passenger.objects.exclude(flights=flight).all(),
		}
	return render(request, "flights/flight.html", context)


def book(request, flight_id):
	passenger_id = int(request.POST['passenger'])
	passenger = Passenger.objects.get(pk=passenger_id)
	flight = Flight.objects.get(pk=flight_id)

	passenger.flights.add(flight)

	return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
