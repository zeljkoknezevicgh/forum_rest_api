from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.views import UserCreateAPIView

urlpatterns = [

    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]

