from django.contrib import admin
from .models import Flight
from .serializers import AdminFlightSerializer

# class FlightAdmin(admin.ModelAdmin):
#     list_display = ('departure_location', 'destination', 'price')  # Include 'price' in the admin list view
#     form = AdminFlightSerializer  # Use the AdminFlightSerializer for the Flight model form

# admin.site.register(Flight, FlightAdmin)

from django.contrib import admin
from django import forms
from .models import Flight

class FlightAdminForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightAdmin(admin.ModelAdmin):
    form = FlightAdminForm  # Use the FlightAdminForm for the admin interface

# Register the Flight model with the custom admin class
admin.site.register(Flight, FlightAdmin)
