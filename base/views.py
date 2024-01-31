
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

from .serializers import RegisterSerializer, UserSerializer

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
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(KnoxLoginView):
    """ API View for user login """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """ Handle POST requests for user login """

        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return Response({'error': 'You are already logged in. Logout to register a new account.'}, status=400)

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class LogoutAPI(generics.GenericAPIView):
    """
    API View for user logout.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user logout.
        """
        request.auth.delete()
        return Response({'detail': 'Successfully logged out'})
