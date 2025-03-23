from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import math

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    # Calculate the read time in mins and seconds of the post based on the average reading speed of 200 words per minute.
    def get_word_count(self):
        words = self.content.split()
        return  len(words)
    
    def get_read_time(self, wpm=200):
        total_secs = self.get_word_count() / wpm * 60
        mins = math.floor(total_secs / 60)
        secs = round(total_secs % 60)
        return mins, secs
              
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"   
