from rest_framework import serializers
from decimal import Decimal, ROUND_DOWN
from .models import Booking, Car, CarImage, CarMake, CarModel

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'

class CarmakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'
        
class CarmodelSerializer(serializers.ModelSerializer):
    make_data=CarmakeSerializer(source='make',read_only=True)
    class Meta:
        model = CarModel
        fields = ['id','make','make_data','name']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    cars=CarSerializer(source='car',read_only=True)
    
    class Meta:
        model = Booking
        fields = ('car','cars', 'start_date', 'end_date', 'is_approved', 'total_amount')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        car = instance.car
        car_data = {
            "id": car.id,
            "year": car.year,
            "available": car.available,
            "price_per_day": car.price_per_day,
            "model": {
                "id": car.model.id,
                "make": {
                    "id": car.model.make.id,
                    "name": car.model.make.name,
                },
                "name": car.model.name,
            },
            "image": [self.context['request'].build_absolute_uri(image.image.url) for image in car.car_images.all()]
        }
        data['cars'] = car_data
        return data
    def create(self, validated_data):
        # Check if the selected time for picking falls within the car's available range
        # if (
        #     validated_data['start_date'] == validated_data['car'].start_date
        #     and validated_data['end_date'] == validated_data['car'].end_date
        #     and validated_data['car'].available
        # ):
            # Calculate the duration in hours

            duration = (validated_data['end_date'] - validated_data['start_date']).days

            # Get the price per day and price per hour from the associated Car model as Decimal objects
            price_per_day = Decimal(validated_data['car'].price_per_day)
            # price_per_hour = Decimal(validated_data['car'].price_per_hour)

            # Calculate the total amount as a Decimal
            total_amount = price_per_day * Decimal(duration)

            # Assign the Decimal total_amount to validated_data
            validated_data['total_amount'] = total_amount
            

        # Call the parent class's create() method to create the Booking object
            booking_instance = Booking.objects.create(**validated_data)

            # Return the created Booking object
            return booking_instance
        # else:
        #   raise serializers.ValidationError("Car not available")
    
    def update(self, instance, validated_data):
        # Update the Booking object with the validated_data
        instance.car = validated_data.get('car', instance.car)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)

        # Check if the selected time for picking falls within the car's available range
        # if (
        #     validated_data['start_date'] == validated_data['car'].start_date
        #     and validated_data['end_date'] == validated_data['car'].end_date
        #     and validated_data['car'].available
        # ):
            # Calculate the duration in hours
        duration = (instance.end_date - instance.start_date).days

            # Get the price per day and price per hour from the associated Car model as Decimal objects
        price_per_day = Decimal(instance.car.price_per_day)
            # price_per_hour = Decimal(instance.car.price_per_hour)

            # Calculate the total amount as a Decimal
        total_amount = price_per_day * Decimal(duration)

            # Update the total_amount field
        instance.total_amount = total_amount

        # Save the updated Booking object
        instance.save()

            # Return the updated Booking object
        return instance
        # else:
        #   raise serializers.ValidationError("Car not available")


