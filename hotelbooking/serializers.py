from rest_framework import serializers
from hotelbooking.models import Amenity, Booking, Hotel, HotelImage

class AmenitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields="__all__"

class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields="__all__"

class HotelSerializers(serializers.ModelSerializer):
    amenities = AmenitySerializers(many=True)
    images = HotelImageSerializers(many=True)

    class Meta:
        model = Hotel
        fields = ['id','name', 'price_per_day', 'available', 'description', 'location', 'amenities', 'images']

    def create(self, validated_data):
        amenities_data = validated_data.pop('amenities', [])
        images_data = validated_data.pop('images', [])

        hotel = Hotel.objects.create(**validated_data)

        for amenity in amenities_data:
            amenity_obj, created = Amenity.objects.get_or_create(**amenity)
            hotel.amenities.add(amenity_obj)

        for image in images_data:
            image_obj, created = HotelImage.objects.get_or_create(**image)
            hotel.images.add(image_obj)

        return hotel



class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'hotel', 'check_in_date', 'check_out_date', 'total_amount']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hotel'] = HotelSerializers(instance.hotel).data
        return representation

    def create(self, validated_data):
        hotel = validated_data['hotel']
        check_in_date = validated_data['check_in_date']
        check_out_date = validated_data['check_out_date']

        # Calculate the number of days between check-in and check-out
        delta = check_out_date - check_in_date
        total_days = delta.days

        # Calculate the total amount based on the hotel's price and the number of days
        total_amount = hotel.price_per_day * total_days

        validated_data['total_amount'] = total_amount

        booking = Booking.objects.create(**validated_data)
        return booking


