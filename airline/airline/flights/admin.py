from django.contrib import admin
from flights.models import Airport, Flight


# Register your models here.

class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'code')


admin.site.register(Airport, AirportAdmin)


class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')


admin.site.register(Flight, FlightAdmin)
