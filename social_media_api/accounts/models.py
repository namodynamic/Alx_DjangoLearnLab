from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/' , blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True )
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    @property
    def follower_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.following.count()
