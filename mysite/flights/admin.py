from django.contrib import admin
from flights.models import *

class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)

class PassengerInline(admin.StackedInline):
	model = Passenger.flights.through
	extra = 1

class FlightAdmin(admin.ModelAdmin):
	list_display = ('id','origin','destination', 'duration')
	ordering = ['id']
	inlines = [PassengerInline]
		

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)