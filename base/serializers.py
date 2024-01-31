from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile, Restaurant, Menu, Vote, Feedback, DailyResults


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the CustomUser model used for user retrieval """

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer for user registration """

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # Marked as write-only to ensure it's not included in response data
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Custom method for creating a new user """

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for obtaining an authentication token """

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        """ Validate the user credentials """
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get(
                'request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')

            data['user'] = user
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        return data


class RestaurantSerializer(serializers.ModelSerializer):
    """ Serializers for Restaurant object """

    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    """ Serializers for Menu object """
    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    """ Serializers for Vote object """
    class Meta:
        model = Vote
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """ Serializers for Feedback """
    class Meta:
        model = Feedback
        fields = '__all__'


class DailyResultsSerializer(serializers.ModelSerializer):
    """ Serializers for Daily Results """
    class Meta:
        model = DailyResults
        fields = '__all__'
