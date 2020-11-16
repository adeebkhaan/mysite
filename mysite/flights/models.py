from django.db import models

# Create your models here.
class Airport(models.Model):
	city = models.CharField(max_length=255)
	code = models.CharField(max_length=3)

	def __str__(self):
		return f"{self.city} ({self.code})"

class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()

	def is_valid_flight(self):
		return (self.origin != self.destination) and (self.duration >= 0)

	def __str__(self):
		return f"Flight : {self.id} {self.origin} to {self.destination}"

class Passenger(models.Model):
	first = models.CharField(max_length=25)
	last = models.CharField(max_length=25)
	flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

	def __str__(self):
		return f"{self.first} {self.last}"