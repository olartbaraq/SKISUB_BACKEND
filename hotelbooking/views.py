from django.shortcuts import render

# Create your views here.
from .serializers import HotelSerializer,BookingSerializer
from .models import Hotel,Booking
from rest_framework import viewsets,permissions
class HotelViewSet(viewsets.ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

    # def get_queryset(self):
    #     user=self.request.user
    #     if user.is_staff:
    #         return Booking.objects.all()
    #     elif user.is_authenticated:
    #         return Booking.objects.filter(user=user)
    #     else:
    #         return Booking.objects.none()
    # permission_classes=[permissions.IsAuthenticated]


