from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the CustomUser model used for user retrieval """

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'user_type', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer for user registration """

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'user_type',
                  'phone_number', 'birthdate', 'address')
        # Marked as write-only to ensure it's not included in response data
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Custom method for creating a new user """

        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
