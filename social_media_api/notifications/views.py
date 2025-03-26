from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    List user's notifications
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)



class NotificationMarkReadView(generics.UpdateAPIView):
    """
    Mark notifications as read
    """
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Mark all notifications for the user as read
        Notification.objects.filter(
            recipient=request.user, 
            is_read=False
        ).update(is_read=True)
        
        return Response({
            'detail': 'All notifications marked as read'
        }, status=status.HTTP_200_OK)
