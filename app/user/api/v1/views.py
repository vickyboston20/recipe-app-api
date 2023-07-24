"""
Views for the user API.
"""
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from user.api.v1.serializers import AuthTokenSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Update the authenticated user in the system"""
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class AuthTokenCreateAPIView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
