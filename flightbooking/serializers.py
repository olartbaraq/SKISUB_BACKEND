from rest_framework import serializers
from rest_framework import generics
from .models import Booking, Flight


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [ 'adults', 'children']



# class BookingCreate(serializers.ModelSerializer):
#     serializer_class = BookingSerializer

#     def perform_create(self, serializer):
#         # Retrieve data from serializer
#         departure_location = serializer.validated_data['departure_location']
#         destination = serializer.validated_data['destination']
#         adults = serializer.validated_data['adults']
#         children = serializer.validated_data['children']

#         # Retrieve the flight based on departure_location and destination
#         flight = Flight.objects.get(departure_location=departure_location, destination=destination)

#         # Calculate the total_amount
#         total_amount = (adults * flight.price) + (children * (flight.price * 0.5))

#         # Create the Booking instance with the calculated total_amount
#         serializer.save(flight=flight, total_amount=total_amount)

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"
    def create(self, validated_data):
        flight=Flight.objects.create(
        departure_location=self.validated_data['departure_location'],
        destination=self.validated_data['destination'],
        price=self.validated_data['price'])
        return flight
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['flight','adults','children','total_amount']

    def Create(self, validated_data):
        booking=Booking.objects.create(
            flight=self.validated_data.pop('flight'),
            adults=self.validated_data['adults'],
            children=self.validated_data['children'],
            total_amount=self.validated_data['total_amount']
        )
        
       
    #     return booking
        



class AdminFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # Expose all fields, including 'price', to admin
        