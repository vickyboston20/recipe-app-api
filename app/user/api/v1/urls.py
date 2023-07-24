from django.urls import path

from user.api.v1.views import (AuthTokenCreateAPIView,
                               UserCreateAPIView,
                               UserUpdateAPIView)

app_name = 'user'

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('me/', UserUpdateAPIView.as_view(), name='me'),
    path('token/', AuthTokenCreateAPIView.as_view(), name='token'),
]
