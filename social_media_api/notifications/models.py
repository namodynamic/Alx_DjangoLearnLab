from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class Notification(models.Model):
    
    NOTIFICATION_TYPES = (
        ('like', 'Post Liked'),
        ('comment', 'Post Commented'),
        ('follow', 'New Follower'),
    )

    
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=255)
    target = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)  # track if the notification has been read   
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ('-timestamp',)
        
    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.actor.username} {self.verb}"    
