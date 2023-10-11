from django.urls import include, path
from rest_framework import routers

from hotelbooking.views import HotelBookingViewSet, HotelViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'hotelbooking', HotelBookingViewSet,basename='booking')

urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
]
