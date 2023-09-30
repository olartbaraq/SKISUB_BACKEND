from rest_framework import serializers
from rest_framework import generics
from .models import Booking, Flight


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','flight','adults','children','total_amount','trip_type']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"
    def create(self, validated_data):
        flight=Flight.objects.create(
        departure_location=self.validated_data['departure_location'],
        destination=self.validated_data['destination'],
        adult_price=self.validated_data['adult_price'],
        child_price=self.validated_data['child_price'],
        )
        return flight
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['id','flight','adults','children','total_amount','trip_type']

    def Create(self, validated_data):
        booking=Booking.objects.create(
            flight=self.validated_data.pop('flight'),
            adults=self.validated_data['adults'],
            children=self.validated_data['children'],
            trip_type=self.validated_data['trip_type'],
            total_amount=self.validated_data['total_amount']
        )
        
       
    #     return booking
        



class AdminFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # Expose all fields, including 'price', to admin
        