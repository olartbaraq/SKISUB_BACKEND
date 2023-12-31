# Import necessary modules
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, AdminFlightViewSet, ListBookingViewSet

# Create a router instance
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'bookings', BookingViewSet)
router.register(r'admin-flights', AdminFlightViewSet)
router.register(r'bookinglist', ListBookingViewSet, basename='booking-list')

# Define a custom action route for BookingCreateViewSet
# booking_create_view = BookingCreateViewSet.as_view({
#     'post': 'create_booking',
# })
# router.register(r'bookings-create', BookingCreateViewSet, basename='booking-create')

# Define your app's urlpatterns
urlpatterns = [
    # ... other URL patterns ...

    # Include the router's URLs under 'api/'
    path('bookings/', include(router.urls)),
    
    # Add the custom action URL for booking creation
    # path('flight/bookings-create/create_booking/', booking_create_view, name='booking-create-action'),
]
