from account.models import Skisubuser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class skisubUserSerializer(serializers.ModelSerializer):
    class Meta:
       model=Skisubuser
       fields="__all__"

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Skisubuser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Skisubuser
        fields = "__all__"
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Skisubuser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # created_date=validated_data['created_date'],
            # updated_date=validated_data['updated_date'],
            is_active=validated_data['is_active'],
            # is_user=validated_data['is_user'],
            is_admin=validated_data['is_admin'],
            phone=validated_data['phone'],
            # status=validated_data['status'],
            is_staff=validated_data['is_staff'], 
        )
        user.set_password(validated_data['password'])
        user.save()

        return user