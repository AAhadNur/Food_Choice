from rest_framework import serializers
from .models import CustomUser, Restaurant, Menu, Vote, Feedback, DailyResults


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
