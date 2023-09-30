from skisub.models import BillOperation
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password

# class skisubUserSerializer(serializers.ModelSerializer):
#     class Meta:
#        model=Skisubuser
#        fields="__all__"

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=Skisubuser.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = Skisubuser
#         fields = "__all__"
#         # extra_kwargs = {
#         #     'first_name': {'required': True},
#         #     'last_name': {'required': True}
#         # }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = Skisubuser.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             # created_date=validated_data['created_date'],
#             # updated_date=validated_data['updated_date'],
#             is_active=validated_data['is_active'],
#             # is_user=validated_data['is_user'],
#             is_admin=validated_data['is_admin'],
#             phone=validated_data['phone'],
#             # status=validated_data['status'],
#             is_staff=validated_data['is_staff'],
           

           

#         )

        
#         user.set_password(validated_data['password'])
#         user.save()

#         return user
    
class AirtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillOperation
        fields=['billclass','serviceops','phone','amount']
    def create(self,validated_data):
        airtime=BillOperation.objects.create(
            billclass=validated_data['billclass'],
            serviceops=validated_data['serviceops'],
            phone=validated_data['phone'],
            amount=validated_data['amount']   
        )
        return airtime
    
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillOperation
        fields=['billclass','serviceops','phone','amount','dataplan']
    def create(self,validated_data):
        data=BillOperation.objects.create(
            billclass=validated_data['billclass'],
            serviceops=validated_data['serviceops'],
            phone=validated_data['phone'],
            amount=validated_data['amount'],
            dataplan=validated_data['dataplan'] 
        )
        return data
class BookFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillOperation
        fields=['location','destination','departdate','flightclass','passenger']
    def create(self, validated_data):
        flight=BillOperation.objects.create(
            location=validated_data['location'],
            destination=validated_data['destination'],
            departdate=validated_data['departdate'],
            flightclass=validated_data['flightclass'],
            passenger=validated_data['passenger']
        )
        return flight
    
class CarBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillOperation
        fields=['location','destination','departdate','cartype','passenger']
    
    def create(self, validated_data):
        carbooking=BillOperation.objects.create(
            location=validated_data['location'],
            destination=validated_data['destination'],
            departdate=validated_data['departdate'],
            flightclass=validated_data['cartype'],
            passenger=validated_data['passenger'],
            # dropoffdate=validated_data['dropoffdate']
        )

        return carbooking
class CabletvSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillOperation
        fields=['category','serviceops','smart_card','selectbouquet']
        def create(self,validated_data):
            cable=BillOperation.objects.create(
               category=validated_data['category'],
               serviceops=validated_data['serviceops'],
               smart_card=validated_data['smart_card'],
               selectbouquet=validated_data['selectbouquet']
            )
            return cable

