from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarImageViewSet, CarMakeViewSet, CarModelViewSet, CarViewSet, BookingViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'carimage', CarImageViewSet)
router.register(r'carmake', CarMakeViewSet)
router.register(r'carmodel', CarModelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # Your other URL patterns go here if you have any
    path('api/', include(router.urls)),
]
