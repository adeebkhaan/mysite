from django.test import TestCase, Client
from .models import *

# Create your tests here.
class ModelsTestCase(TestCase):

	def setUp(self):

		#Create Airports
		a1 = Airport.objects.create(code="AAA", city="City A")
		a2 = Airport.objects.create(code="BBB", city="City B")

		#Create Flights
		Flight.objects.create(origin=a1, destination=a2, duration=550)
		Flight.objects.create(origin=a1, destination=a1, duration=550)
		Flight.objects.create(origin=a1, destination=a2, duration=-550)
	
	def test_departures_count(self):
		a = Airport.objects.get(code="AAA")
		self.assertEqual(a.departures.count(), 3)

	def test_arrivals_count(self):
		a = Airport.objects.get(code="AAA")
		self.assertEqual(a.arrivals.count(), 1)

	def test_valid_flight(self):
		a1 = Airport.objects.get(code="AAA")
		a2 = Airport.objects.get(code="BBB")
		f = Flight.objects.get(origin=a1, destination=a2, duration=550)

		self.assertTrue(f.is_valid_flight())

	def test_invalid_flight_destination(self):
		a1 = Airport.objects.get(code="AAA")
		f = Flight.objects.get(origin=a1, destination=a1, duration=550)

		self.assertFalse(f.is_valid_flight())

	def test_invalid_flight_duration(self):
		a1 = Airport.objects.get(code="AAA")
		a2 = Airport.objects.get(code="BBB")
		f = Flight.objects.get(origin=a1, destination=a2, duration=-550)

		self.assertFalse(f.is_valid_flight())

	def test_index(self):
		c = Client()
		response = c.get("/flights/")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['Allflights'].count(), 3)

	def test_valid_flight_page(self):

		a1 = Airport.objects.get(code='AAA')
		a2 = Airport.objects.get(code='BBB')
		f = Flight.objects.get(origin=a1, destination=a2, duration=550)

		c = Client()
		response = c.get(f"/flights/{f.id}/")
		self.assertEqual(response.status_code, 200)

	def test_passengers_on_flight(self):
		f = Flight.objects.get(id=1)
		p = Passenger.objects.create(first='Adeeb', last='Khan')
		
		f.passengers.add(p)
		
		c = Client()
		response = c.get(f"/flights/{f.id}/")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['passengers'].count(), 1)

	def test_non_passengers_on_flight(self):
		f = Flight.objects.get(id=2)
		p = Passenger.objects.create(first='Adnan', last='Gujjar')

		c = Client()
		response = c.get(f"/flights/{f.id}/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['non_passengers'].count(), 1)



