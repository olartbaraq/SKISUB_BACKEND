from rest_framework import serializers
from decimal import Decimal, ROUND_DOWN
from .models import Hotel, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    hotel_data = HotelSerializer(source='hotel', read_only=True)
    class Meta:
        model = Booking
        fields = ('id','hotel_data','hotel', 'check_in_date', 'check_out_date', 'total_amount')

    def create(self, validated_data):
        # Calculate the duration in days
        duration = (validated_data['check_out_date'] - validated_data['check_in_date']).days

        # Get the price per day from the associated Hotel model as Decimal
        price_per_day = Decimal(validated_data['hotel'].price_per_day)

        # Calculate the total amount as a Decimal
        total_amount = price_per_day * Decimal(duration)

        # Assign the Decimal total_amount to validated_data
        validated_data['total_amount'] = total_amount

        # Call the parent class's create() method to create the Booking object
        booking_instance = Booking.objects.create(**validated_data)

        # Return the created Booking object
        return booking_instance

    def update(self, instance, validated_data):
        # Update the Booking object with the validated_data
        instance.hotel = validated_data.get('hotel', instance.hotel)
        instance.check_in_date = validated_data.get('check_in_date', instance.check_in_date)
        instance.check_out_date = validated_data.get('check_out_date', instance.check_out_date)

        # Calculate the duration in days
        duration = (instance.check_out_date - instance.check_in_date).days

        # Get the price per day from the associated Hotel model as Decimal
        price_per_day = Decimal(instance.hotel.price_per_day)

        # Calculate the total amount as a Decimal
        total_amount = price_per_day * Decimal(duration)

        # Update the total_amount field
        instance.total_amount = total_amount

        # Save the updated Booking object
        instance.save()

        # Return the updated Booking object
        return instance
