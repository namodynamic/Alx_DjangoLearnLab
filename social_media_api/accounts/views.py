from rest_framework.views import APIView
from .serializers import CustomUserRegistrationSerializer, UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from .models import CustomUser


class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = serializer.data
            response_data['user'] = UserProfileSerializer(user).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserProfileSerializer(user).data
        })
    
    
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# class FollowUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, user_id):
#         try:
#             user_to_follow = CustomUser.objects.get(id=user_id)
#             # Prevent following yourself
#             if request.user == user_to_follow:
#                 return Response(
#                     {"detail": "You cannot follow yourself."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             # Check if already following
#             if request.user.following.filter(id=user_to_follow.id).exists():
#                 return Response(
#                     {"detail": "You are already following this user."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             # Add the follow relationship
#             request.user.following.add(user_to_follow)
#             return Response(
#                 {"detail": f"You are now following {user_to_follow.username}."},
#                 status=status.HTTP_200_OK
#             )
#         except CustomUser.DoesNotExist:
#             return Response(
#                 {"detail": "User not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#     def delete(self, request, user_id):
#         try:
#             user_to_unfollow = CustomUser.objects.get(id=user_id)
#             # Check if actually following
#             if not request.user.following.filter(id=user_to_unfollow.id).exists():
#                 return Response(
#                     {"detail": "You are not following this user."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             # Remove the follow relationship
#             request.user.following.remove(user_to_unfollow)
#             return Response(
#                 {"detail": f"You have unfollowed {user_to_unfollow.username}."},
#                 status=status.HTTP_200_OK
#             )
#         except CustomUser.DoesNotExist:
#             return Response(
#                 {"detail": "User not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )



class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = self.get_queryset().get(id=user_id)
            if request.user == user_to_follow:
                raise ValidationError({"detail": "You cannot follow yourself."})
            if request.user.following.filter(id=user_to_follow.id).exists():
                raise ValidationError({"detail": "You are already following this user."})
            request.user.following.add(user_to_follow)
            return Response(
                {"detail": f"You are now following {user_to_follow.username}."},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
           

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id):
        try:
            user_to_unfollow = self.get_queryset().get(id=user_id)
            if not request.user.following.filter(id=user_to_unfollow.id).exists():
                raise ValidationError({"detail": "You are not following this user."})
            request.user.following.remove(user_to_unfollow)
            return Response(
                {"detail": f"You have unfollowed {user_to_unfollow.username}."},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )                      
              