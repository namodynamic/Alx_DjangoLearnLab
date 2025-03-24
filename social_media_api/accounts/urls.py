from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, FollowUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user')
]