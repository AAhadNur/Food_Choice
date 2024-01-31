from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth import login

from .serializers import (
    RegisterSerializer, UserSerializer, RestaurantSerializer,
    MenuSerializer, VoteSerializer, FeedbackSerializer, DailyResultsSerializer
)
from . models import Restaurant, Menu, Feedback, DailyResults, Vote, Profile
from .permissions import IsAdminOrOwner, IsEmployee, IsAdministrator

# Create your views here.


# Register API
class RegisterAPI(generics.GenericAPIView):
    """ API View for user registration """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """ Handle POST requests for user registration """

        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return Response({'error': 'You are already logged in. Logout to register a new account.'}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Profile.objects.create(
            user=user,
            fullname=user.username
        )

        # Automatically login
        login(request, user)

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    """ API View for user login using Knox """
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthTokenSerializer

    def post(self, request, format=None):
        """ Handle POST requests for user login """

        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return Response({'error': 'You are already logged in. Logout to login with a different account.'}, status=400)

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Log in the user
        login(request, user)

        # Generate a new token for the user using Knox
        _, token = AuthToken.objects.create(user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token,  # Include the Knox authentication token in the response
            "details": "Logged in successfully",
        })


class LogoutAPI(generics.GenericAPIView):
    """
    API View for user logout.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user logout.
        """
        AuthToken.objects.filter(user=request.user).delete()
        return Response({'detail': 'Successfully logged out'})


class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    """ API view for listing all restaurants and creating new ones """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]

    def perform_create(self, serializer):
        """ Perform creation of a new restaurant """
        serializer.save()


class RestaurantDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ API view for retrieving, updating, and deleting individual restaurants """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]


class MenuListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all menus and creating new ones.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]


class MenuDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting individual menus.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]


class CurrentDayMenuAPIView(generics.ListAPIView):
    """
    API view for retrieving the menu for the current day.
    """

    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Get the menu items for the current day.
        """
        current_day_menu = Menu.objects.filter(
            date=timezone.now().date()
        )
        return current_day_menu


class VoteCreateAPIView(generics.CreateAPIView):
    """
    API view for allowing employee-type users to vote on a specific menu.
    """

    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def perform_create(self, serializer):
        """
        Perform the creation of a new vote.
        """
        serializer.save(voter=self.request.user)


class FeedbackListAPIView(generics.ListAPIView):
    """
    API view for listing all feedbacks.
    """

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedbackCreateAPIView(generics.CreateAPIView):
    """
    API view for creating new feedback.
    """
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployee]

    def perform_create(self, serializer):
        """
        Perform the creation of a new feedback.

        Set the employee providing feedback to the current authenticated user.
        """
        serializer.save(employee=self.request.user)


class DailyResultsListAPIView(generics.ListAPIView):
    """
    API view for listing all DailyResults.
    """

    queryset = DailyResults.objects.all()
    serializer_class = DailyResultsSerializer
    permission_classes = [permissions.IsAuthenticated]


class DailyResultsCreateAPIView(generics.ListCreateAPIView):
    """ API for finding out the winning restaurant of current date """
    queryset = DailyResults.objects.all()
    serializer_class = DailyResultsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """ 
            This method will search for current_date winning restaurant.
            If it will not get any then it will count all the votes that was cast
            in the current date.
            Then, it will check if winning restaurant which contains the winning menu
            has winning_strike of 3 consecutive working days. If yes then winning_strike will
            be set to 0. Otherwise, winning_strike will be incremented by 1.
        """

        # Checks if winner restaurant of current date already selected
        current_date_results = DailyResults.objects.filter(
            result_date=timezone.now().date()
        )

        # If no winner selected yet
        if current_date_results is None:
            today = timezone.now().date()
            print(today)

            # Vote count of menus based on current date
            menu_votes_count = Vote.objects.filter(
                vote_timestamp=today
            ).values('menu').annotate(vote_count=Count('id'))
            print(menu_votes_count)

            menu_with_max_votes = menu_votes_count.order_by(
                '-vote_count').all()
            print(menu_with_max_votes)

            winning_menu = None
            winning_restaurant = None

            # Resolves the winning strike of 3 consecutive working days
            for menu in menu_with_max_votes:
                menu_id = menu['menu']
                winning_menu = Menu.objects.get(id=menu_id)
                winning_restaurant = winning_menu.restaurant
                max_votes = menu['vote_count']

                if winning_restaurant.winning_strike > 2:
                    winning_restaurant.winning_strike = 0
                    winning_restaurant.save()
                else:
                    winning_restaurant.winning_strike += 1
                    winning_restaurant.save()
                    break

            # Winning restaurant and it's menu gets added in the Dailyresult table
            if winning_menu is not None and winning_restaurant is not None:
                DailyResults.objects.create(
                    winning_menu=winning_menu,
                    winning_restaurant=winning_restaurant,
                    votecount=max_votes
                )

            return Response({
                'winning menu': winning_menu,
                'winning restaurent': winning_restaurant,
                'details': 'helllow'
            })


class DailyResultsCurrentDateAPIView(generics.RetrieveAPIView):
    """
    API view for retrieving the DailyResults of the current date based on votecount.
    """

    serializer_class = DailyResultsSerializer
    lookup_field = 'votecount'
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Get the DailyResults instance for the current date based on votecount.
        """
        current_date_results = DailyResults.objects.filter(
            result_date=timezone.now().date()
        ).order_by('-votecount').first()

        if current_date_results is not None:
            return current_date_results
        else:
            # If no results found
            return Response({'detail': 'No DailyResults found for the current date.'}, status=404)
