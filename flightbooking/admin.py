from django.contrib import admin


from .models import Flight, Booking
# from .serializers import AdminFlightSerializer

# # class FlightAdmin(admin.ModelAdmin):
# #     list_display = ('departure_location', 'destination', 'price')  # Include 'price' in the admin list view
# #     form = AdminFlightSerializer  # Use the AdminFlightSerializer for the Flight model form

# # admin.site.register(Flight, FlightAdmin)

# from django.contrib import admin
# from django import forms
# from .models import Flight

# class FlightAdminForm(forms.ModelForm):
#     class Meta:
#         model = Flight
#         fields = '__all__'

# class FlightAdmin(admin.ModelAdmin):
#     form = FlightAdminForm  # Use the FlightAdminForm for the admin interface

# # Register the Flight model with the custom admin class
# admin.site.register(Flight, FlightAdmin)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('departure_location', 'destination', 'adult_price', 'child_price', 'departure_date', 'return_date', 'trip_type', 'select_class')
    list_filter = ('trip_type', 'select_class')
    search_fields = ('departure_location', 'destination')
    list_editable = ('trip_type', 'select_class')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('flight', 'adults', 'children', 'departure_date', 'return_date', 'trip_type', 'select_class', 'total_amount')
    list_filter = ('flight__trip_type', 'flight__select_class')
    search_fields = ('flight__departure_location', 'flight__destination')
    list_editable = ('trip_type', 'select_class')

# Register your custom admin classes with the Django admin site
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)