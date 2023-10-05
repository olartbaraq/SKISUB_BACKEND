from rest_framework import routers
from django.urls import path, include
from .views import HotelViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet,basename='hotel')
router.register(r'bookings', BookingViewSet,basename='customhotel')

urlpatterns = [
    path('', include(router.urls)),
    # Add any custom API endpoints or URL patterns as needed
]
